# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
# rojos.


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        # Inicializa los atributos de la cuenta
        self.titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        # Getter para el titular
        return self._titular

    @titular.setter
    def titular(self, valor):
        # Setter para el titular
        self._titular = valor

    @property
    def cantidad(self):
        # Getter para la cantidad
        return self._cantidad

    def mostrar(self):
        # Muestra los datos de la cuenta
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        # Ingresa una cantidad en la cuenta si es positiva
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        # Retira una cantidad de la cuenta
        self._cantidad -= cantidad

# Ejemplo de uso
titular = Persona("Juan", 20, "12345678A")
cuenta = Cuenta(titular, 100.0)
cuenta.mostrar()  # Salida: Titular: <__main__.Persona object at 0x7f5c3b3b7d60>, Cantidad: 100.0
cuenta.ingresar(50)
cuenta.mostrar()  # Salida: Titular: <__main__.Persona object at 0x7f5c3b3b7d60>, Cantidad: 150.0
cuenta.retirar(20)
cuenta.mostrar()  # Salida: Titular: <__main__.Persona object at 0x7f5c3b3b7d60>, Cantidad: 130.0
