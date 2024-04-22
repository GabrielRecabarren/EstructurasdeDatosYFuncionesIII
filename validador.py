def validate(opciones, eleccion):
    while eleccion not in opciones:
        print('Opción no válida, ingrese una de las opciones válidas:', opciones)
        eleccion = input('Ingrese una opción válida: ').lower()
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    numeros = ['0', '1']
    eleccion_validada = validate(numeros, eleccion)
    print('Opción válida ingresada:', eleccion_validada)
