# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
# ejercicio tanto de manera iterativa como recursiva.

def get_int():
    # Bucle infinito hasta que se reciba un valor válido
    while True:
        try:
            # Intentar convertir la entrada del usuario a entero
            valor = int(input("Introduce un número entero: "))
            # Devolver el valor si es correcto
            return valor
        except ValueError:
            # Si se produce una excepción, mostrar un mensaje y repetir
            print("Valor no válido. Inténtalo de nuevo.")

# Ejemplo de uso
print(get_int())

def get_int_recursivo():
    try:
        # Intentar convertir la entrada del usuario a entero
        return int(input("Introduce un número entero: "))
    except ValueError:
        # Si se produce una excepción, mostrar un mensaje y llamar recursivamente a la función
        print("Valor no válido. Inténtalo de nuevo.")
        return get_int_recursivo()

# Ejemplo de uso
print(get_int_recursivo())
