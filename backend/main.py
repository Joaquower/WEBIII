import datetime
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use service name + credentials from docker-compose
client = MongoClient("mongodb://admin_user:web3@mongo:27017/")
database = client.practica1
collection_historial = database.historial

@app.get("/calculator/sum")
def sum_numbers(a: float, b: float):
    result = a + b

    document = {
        "a": a,
        "b": b,
        "result": result,
        "date": datetime.datetime.now(tz=datetime.timezone.utc)
    }

    collection_historial.insert_one(document)

    return {"a": a, "b": b, "result": result}

@app.get("/calculator/history")
def obtain_history():
    records = collection_historial.find().sort("date", -1).limit(10)

    history = []
    for record in records:
        history.append({
            "a": record.get("a"),
            "b": record.get("b"),
            "result": record.get("result"),
            "date": record["date"].isoformat() if "date" in record else None
        })

    return {"history": history}
