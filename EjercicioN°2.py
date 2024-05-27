# Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm(a, b):
    # El MCM se calcula utilizando el MCD
    return abs(a * b) // mcd(a, b)

# Ejemplo de uso
print(mcm(54, 24))  # Salida: 216
