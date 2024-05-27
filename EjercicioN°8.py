#  Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
# cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        # Inicializa los atributos de la cuenta joven heredando de Cuenta
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        # Getter para la bonificación
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, valor):
        # Setter para la bonificación
        self._bonificacion = valor

    def es_titular_valido(self):
        # Devuelve True si el titular es mayor de edad pero menor de 25 años
        return 18 <= self.titular.edad < 25

    def retirar(self, cantidad):
        # Permite retirar dinero sólo si el titular es válido
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")

    def mostrar(self):
        # Muestra los datos de la cuenta joven
        print(f"Cuenta Joven\nTitular: {self.titular.nombre}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")

# Ejemplo de uso
titular_joven = Persona("Ana", 22, "87654321B")
cuenta_joven = CuentaJoven(titular_joven, 200.0, 10)
cuenta_joven.mostrar()  # Salida: Cuenta Joven\nTitular: Ana, Cantidad: 200.0, Bonificación: 10%
print(cuenta_joven.es_titular_valido())  # Salida: True
cuenta_joven.retirar(50)
cuenta_joven.mostrar()  # Salida: Cuenta Joven\nTitular: Ana, Cantidad: 150.0, Bonificación: 10%
