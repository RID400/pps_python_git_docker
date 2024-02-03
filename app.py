from flask import Flask, jsonify, request
from bayeta import frotar, insertar_nueva_frase_en_mongo

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola, mundo'

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases_auspiciosas": frases})

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    try:
        # Obtener el JSON del cuerpo de la solicitud
        data = request.get_json()

        # Verificar si el JSON contiene la clave 'frases' con una lista de frases
        if 'frases' in data and isinstance(data['frases'], list):
            nuevas_frases = data['frases']

            # Llamar a la función de inserción para cada nueva frase
            for nueva_frase in nuevas_frases:
                insertar_nueva_frase_en_mongo(nueva_frase)

            # Devolver código de respuesta 200 si todo es exitoso
            return jsonify({"message": "Frases agregadas exitosamente"}), 200
        else:
            # Devolver código de respuesta 400 si el formato no es correcto
            return jsonify({"error": "Formato JSON incorrecto. Se esperaba una lista de frases"}), 400
    except Exception as e:
        # Manejar cualquier excepción y devolver código de respuesta 500
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == '__main__':
    # Modificar la línea para que Flask escuche en todas las interfaces
    app.run(host='0.0.0.0', port=5000, debug=True)
