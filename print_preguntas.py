def print_pregunta(enunciado, alternativas):
    print(enunciado)
    letras = ['A', 'B', 'C', 'D']
    for i, (alt, _) in enumerate(alternativas):
        print(f"{letras[i]}. {alt}")

if __name__ == '__main__':
    # Verificar que las preguntas y alternativas se muestren según lo indicado
    pregunta = ("Enunciado básico 1", [['alt_1', 0], ['alt_2', 1], ['alt_3', 0], ['alt_4', 0]])
    print_pregunta(pregunta[0], pregunta[1])
