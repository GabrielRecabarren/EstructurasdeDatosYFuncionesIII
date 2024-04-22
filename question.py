import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}

def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]

    # Escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    pregunta_elegida = preguntas[f"pregunta_{n_elegido}"]

    # Eliminarla del conjunto de opciones para no volverla a escoger
    opciones[dificultad].remove(n_elegido)

    # Escoger enunciado y alternativas mezcladas
    enunciado = pregunta_elegida['enunciado']
    alternativas = shuffle_alt(pregunta_elegida)

    return enunciado, alternativas

if __name__ == '__main__':
    # Verificar que las preguntas cambian de orden y no se repiten
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
