import subprocess
import json
import random
from typing import List

def obtener_frases_desde_mongo(n_frases: int = 1) -> List[str]:
    # Llamar al script de MongoDB para obtener frases
    proceso = subprocess.run(['python', 'mongo.py'], capture_output=True, text=True)

    # Verificar si la ejecución fue exitosa y si hay salida
    if proceso.returncode == 0 and proceso.stdout.strip():
        # Obtener las frases desde la salida del script de MongoDB
        frases_json = proceso.stdout.strip()
        frases = json.loads(frases_json)
        return frases
    else:
        # Manejar errores, imprimir mensaje y devolver lista vacía
        print(f"Error al obtener frases desde MongoDB: {proceso.stderr}")
        return []

def insertar_nueva_frase_en_mongo(nueva_frase: str):
    # Llamar al script de MongoDB para insertar la nueva frase
    subprocess.run(['python', 'mongo.py', 'insertar', nueva_frase])

def frotar(n_frases: int = 1) -> List[str]:
    # Intentar obtener frases desde MongoDB
    frases_auspiciosas = obtener_frases_desde_mongo(n_frases)

    # Elegir N frases aleatorias
    frases_elegidas = random.sample(frases_auspiciosas, n_frases)

    # Devolver la lista de frases
    return frases_elegidas

if __name__ == "__main__":
    # Uso de la función de inserción
    nueva_frase = "Nueva frase auspiciosa"
    insertar_nueva_frase_en_mongo(nueva_frase)

    # Uso de la función para obtener frases
    frases_obtenidas = frotar(3)

    # Imprimir las frases obtenidas
    for frase in frases_obtenidas:
        print(frase)
