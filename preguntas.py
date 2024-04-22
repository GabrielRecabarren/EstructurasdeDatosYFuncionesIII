preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál es el color del cielo?'],
    'alternativas': [['Azul', 1], 
                     ['Celeste', 0], 
                     ['Rojo', 0], 
                     ['Fucsia', 0]]},
    'pregunta_2': {'enunciado':['¿Cuántos días tiene una semana?'],
    'alternativas': [['5 días', 0], 
                     ['6 días', 0], 
                     ['7 días', 1], 
                     ['8 días', 0]]},
    'pregunta_3': {'enunciado':['¿Qué animal hace "mu"?'],
    'alternativas': [['Perro', 0], 
                     ['Gato', 0], 
                     ['Cabra', 0], 
                     ['Vaca', 1]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Cuál es el resultado de 2 + 2?'],
    'alternativas': [['3', 0], 
                     ['4', 1], 
                     ['5', 0], 
                     ['10', 0]]},
    'pregunta_2': {'enunciado':['¿Quién escribió "Don Quijote de la Mancha"?'],
    'alternativas': [['Shakespeare', 0], 
                     ['Cervantes', 1], 
                     ['Hemingway', 0], 
                     ['Tolkien', 0]]},
    'pregunta_3': {'enunciado':['¿Cuál es el río más largo del mundo?'],
    'alternativas': [['Nilo', 0], 
                     ['Amazonas', 0], 
                     ['Yangtsé', 0], 
                     ['Misisipi', 1]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Quién pintó la Mona Lisa?'],
    'alternativas': [['Da Vinci', 1], 
                     ['Van Gogh', 0], 
                     ['Picasso', 0], 
                     ['Rembrandt', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es el planeta más grande del sistema solar?'],
    'alternativas': [['Tierra', 0], 
                     ['Marte', 0], 
                     ['Júpiter', 1], 
                     ['Saturno', 0]]},
    'pregunta_3': {'enunciado':['¿Quién fue el primer presidente de Estados Unidos?'],
    'alternativas': [['Lincoln', 0], 
                     ['Washington', 1], 
                     ['Roosevelt', 0], 
                     ['Kennedy', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}
