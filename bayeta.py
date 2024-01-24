# bayeta.py
import random

def frotar(n_frases: int = 1) -> list:
	# Cargar frases desde el fichero frases.txt
	with open('frases.txt', 'r') as file:
		frases_auspiciosas = [line.strip() for line in file]

	# Elegir N frases aleatorias
	frases_elegidas = random.sample(frases_auspiciosas, n_frases)

	# Devolver la lista de frases
	return frases_elegidas
