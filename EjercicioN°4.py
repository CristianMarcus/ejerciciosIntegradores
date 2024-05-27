# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
# palabra más repetida y su frecuencia.

#palabra mas repetida

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

def palabra_mas_repetida(frecuencia):
    # Encontrar la palabra con la frecuencia más alta
    max_palabra = max(frecuencia, key=frecuencia.get)
    # Devolver una tupla con la palabra más repetida y su frecuencia
    return (max_palabra, frecuencia[max_palabra])

# Ejemplo de uso
cadena = "hola mundo hola"
frecuencia = frecuencia_palabras(cadena)
print(palabra_mas_repetida(frecuencia))  # Salida: ('hola', 2)
