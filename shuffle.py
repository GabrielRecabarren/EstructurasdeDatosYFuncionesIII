import preguntas as p
import random

def shuffle_alt(pregunta):
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    # Verificar que las alternativas se mezclan de manera aleatoria
    pregunta_ejemplo = p.pool_preguntas['basicas']['pregunta_1']
    print(shuffle_alt(pregunta_ejemplo))
