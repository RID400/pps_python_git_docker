from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola, mundo'

@app.route('/frotar/<int:n_frases>')
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases_auspiciosas": frases})

if __name__ == '__main__':
    # Modificar la línea para que Flask escuche en todas las interfaces
    app.run(host='0.0.0.0', port=5000, debug=True)
