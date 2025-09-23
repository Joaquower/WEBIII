import { useState, useEffect } from 'react'

function App() {
    const [a, setA] = useState("");
    const [b, setB] = useState("");
    const [resultado, setResultado] = useState(null);
    const [historial, setHistorial] = useState([]);

    const sumar = async () => {
        const res = await fetch(`http://localhost:8089/calculator/sum?a=${a}&b=${b}`);
        const data = await res.json();
        setResultado(data.result);
        obtenerHistorial();
    };

    const obtenerHistorial = async () => {
        const res = await fetch("http://localhost:8089/calculator/history");
        const data = await res.json();
        setHistorial(data.history);
    };

    useEffect(() => {
        (async () => {
            await obtenerHistorial();
        })();
    }, [resultado]);

    return (
        <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col items-center p-6">
            <div className="w-full max-w-md bg-gray-800 rounded-xl shadow-lg p-6">
                <h1 className="text-3xl font-bold text-center text-blue-400 mb-6">
                    Calculadora
                </h1>

                {/* Inputs */}
                <div className="flex flex-col space-y-4">
                    <input
                        type="number"
                        value={a}
                        onChange={(e) => setA(e.target.value)}
                        placeholder="Número 1"
                        className="px-4 py-2 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <input
                        type="number"
                        value={b}
                        onChange={(e) => setB(e.target.value)}
                        placeholder="Número 2"
                        className="px-4 py-2 rounded-lg bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <button
                        onClick={sumar}
                        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg transition duration-200"
                    >
                        Sumar
                    </button>
                </div>

                {/* Resultado */}
                {resultado !== null && (
                    <h2 className="mt-6 text-xl font-semibold text-green-400 text-center">
                        Resultado: {resultado}
                    </h2>
                )}

                {/* Historial */}
                <div className="mt-8">
                    <h3 className="text-lg font-semibold text-gray-300 mb-3">Historial:</h3>
                    <ul className="space-y-2 max-h-40 overflow-y-auto">
                        {historial.map((op, i) => (
                            <li
                                key={i}
                                className="bg-gray-700 px-4 py-2 rounded-lg border border-gray-600 text-sm"
                            >
                                {op.a} + {op.b} ={" "}
                                <span className="text-green-400 font-bold">{op.result}</span>{" "}
                                <span className="text-gray-400 text-xs">({op.date})</span>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default App;
