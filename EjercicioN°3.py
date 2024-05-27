# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def frecuencia_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    # Crear un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    # Iterar sobre cada palabra en la lista
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementar su contador
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        # Si la palabra no está en el diccionario, añadirla con un contador de 1
        else:
            frecuencia[palabra] = 1
    # Devolver el diccionario de frecuencias
    return frecuencia

# Ejemplo de uso
cadena = "hola mundo hola"
print(frecuencia_palabras(cadena))  # Salida: {'hola': 2, 'mundo': 1}

 
