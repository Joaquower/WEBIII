# Light based image for python 3.13
FROM mirror.gcr.io/library/python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements
COPY requirements.txt .

# Install depencencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code of the app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]