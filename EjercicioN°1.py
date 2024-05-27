#1. Escribir una función que calcule el máximo común divisor entre dos números.

def mcd(a, b):
    # Mientras b no sea cero
    while b:
        # Asignar a 'a' el valor de 'b' y a 'b' el resto de 'a' dividido por 'b'
        a, b = b, a % b
    # Devolver el valor de 'a' que es el MCD
    return a

# Ejemplo de uso
print(mcd(54, 24))  # Salida: 6
