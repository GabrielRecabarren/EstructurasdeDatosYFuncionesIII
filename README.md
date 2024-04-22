# Trivia App

Este es un programa en Python que simula una trivia interactiva con preguntas de diferentes niveles de dificultad. El jugador puede elegir la cantidad de preguntas por nivel y gana al responder todas correctamente. Las preguntas aparecen en un orden aleatorio y las alternativas se mezclan cada vez que se ejecuta la aplicación.

## Cómo usar el programa

1. Descarga todos los archivos del repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Abre una terminal en la ubicación de los archivos.
4. Ejecuta el siguiente comando para iniciar la trivia:

```bash
python main.py
```

5. Sigue las instrucciones en pantalla para jugar la trivia.

## Requerimientos

### 1. Validador (1 Punto)
El archivo `validador.py` contiene una función `validate()` que permite validar si un valor se encuentra incluido en un conjunto de opciones.

### 2. Escoger nivel (1 Punto)
El archivo `level.py` incluye la función `choose_level()` que permite escoger el nivel de dificultad de la pregunta a realizar.

### 3. Mezclar alternativas (1 Punto)
El archivo `shuffle.py` contiene la función `shuffle_alt()` que mezcla las alternativas de una pregunta.

### 4. Escoger una pregunta (2 Puntos)
El archivo `question.py` permite escoger una pregunta que no se haya hecho durante la ejecución del programa dependiendo del nivel de dificultad.

### 5. Mostrar las preguntas en pantalla (1 Punto)
El archivo `print_preguntas.py` contiene la función `print_pregunta()` que muestra las preguntas en pantalla con un formato específico.

### 6. Verificar respuesta (1 Punto)
El archivo `verify.py` incluye la función `verificar()` que permite comprobar si la respuesta entregada por el usuario es correcta.

### 7. Ensamblado de la app (3 Puntos)
El archivo `main.py` ensambla todas las funcionalidades anteriores y permite jugar la trivia de acuerdo a las reglas establecidas.

## Autor
[GabrielRecabarren](https://github.com/GabrielRecabarren)
