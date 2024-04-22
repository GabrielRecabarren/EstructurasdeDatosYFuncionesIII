def verificar(alternativas, eleccion):
    # Devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)

    # Lógica para determinar respuestas correctas
    for i, (_, correcta) in enumerate(alternativas):
        if correcta == 1 and i == eleccion:
            print('Respuesta Correcta')
            return True
    print('Respuesta Incorrecta')
    return False

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    import preguntas as p
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
