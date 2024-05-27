# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        # Inicializa los atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        # Getter para el nombre
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Setter para el nombre
        self._nombre = valor

    @property
    def edad(self):
        # Getter para la edad
        return self._edad

    @edad.setter
    def edad(self, valor):
        # Setter para la edad con validación de que no sea negativa
        if valor >= 0:
            self._edad = valor
        else:
            raise ValueError("La edad no puede ser negativa")

    @property
    def dni(self):
        # Getter para el DNI
        return self._dni

    @dni.setter
    def dni(self, valor):
        # Setter para el DNI
        self._dni = valor

    def mostrar(self):
        # Muestra los datos de la persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        # Devuelve True si la persona es mayor de edad
        return self.edad >= 18

# Ejemplo de uso
persona = Persona("Juan", 20, "12345678A")
persona.mostrar()  # Salida: Nombre: Juan, Edad: 20, DNI: 12345678A
print(persona.es_mayor_de_edad())  # Salida: True
