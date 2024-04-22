def choose_level(n_pregunta, p_level):
    if p_level == 1:
        if n_pregunta <= 2:
            level = 'basicas'
        elif 2 < n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 2:
        if n_pregunta <= 3:
            level = 'basicas'
        elif 3 < n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif 3 < n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    return level

if __name__ == '__main__':
    # Verificar resultados
    print(choose_level(2, 2))  # Básicas
    print(choose_level(3, 2))  # Intermedias
    print(choose_level(7, 2))  # Avanzadas
    print(choose_level(4, 3))  # Intermedias
