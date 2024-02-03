from pymongo import MongoClient
import json

def obtener_todas_frases():
    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://localhost:27017/')

    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']

    # Conexión con la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']

    # Obtener todas las frases
    todas_frases = list(frases_auspiciosas.find())

    # Imprimir las frases en formato JSON
    frases_json = json.dumps([{'frase': frase['frase']} for frase in todas_frases], ensure_ascii=False)
    print(frases_json)

    # Cerrar cliente
    cliente_mongo.close()

if __name__ == "__main__":
    obtener_todas_frases()
