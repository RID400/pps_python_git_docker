from pymongo import MongoClient
import json

def inicializar():
    # Cargar frases desde el archivo de texto
    with open('frases.txt', 'r', encoding='utf-8') as file:
        # Leer líneas del archivo y eliminar caracteres de nueva línea
        datos = [{'frase': linea.strip()} for linea in file.readlines()]

    # Conexión con el motor de Mongo
    cliente_mongo = MongoClient('mongodb://mongo:27017/')

    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']

    # Conexión con la tabla (llamada colección en Mongo)
    frases_auspiciosas = bd['frases_auspiciosas']

    # Verificar si ya existen datos en la colección
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos solo si no existen previamente
        frases_auspiciosas.insert_many(datos)

    # Obtener todas las frases
    todas_frases = list(frases_auspiciosas.find())

    # Imprimir las frases en formato JSON
    frases_json = json.dumps([{'frase': frase['frase']} for frase in todas_frases], ensure_ascii=False)
    print(frases_json)

    # Cerrar cliente
    cliente_mongo.close()

if __name__ == "__main__":
    inicializar()
