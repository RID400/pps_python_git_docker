from flask import Flask, jsonify

def frotar(n_frases: int = 1) -> list:
	frase = "Hola Mundo"
	return [frase] * n_frases
