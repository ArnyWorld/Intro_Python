#Una clase debe comenzar con una Mayúscula 
class Alumno:
    #Constructor
    def __init__(self, nombre, registro,sexo, semestre):
        """Por defecto los atributos son públicos, si se quiere 
        cambiar a privado la variable debe comenzar con doble barra baja (__nombreVariable)
        si se quiere manejar una variable protegida debe comenzar con una barra baja (_nombreVariable)
        """
        self.nombre = nombre
        self.__registro = registro
        self.sexo = sexo
        self.semestre = semestre
            
    def mostrar_informacion(self):
        print(f'Nombre :{self.nombre}, Registro: {self.__registro}, Sexo: {self.sexo}, Semestre: {self.semestre}')
#Intanciando la clase

#GETTERS Y SETTERS |||  Get = Obtener valor     Set = Asignar valor
    def get_registro(self):
        return self.__registro
        
    def set_registro(self, registro):
        self.__registro = registro


alumno = Alumno('Gary Nova','125456','Masculino','1er semestre')
alumno.mostrar_informacion()
alumno.set_registro(123456)
print(alumno.get_registro())

alumno2 = Alumno('Sarai Blanco','125987','Femenino','8vo semestre')
alumno2.mostrar_informacion()
alumno.set_registro(987654)
print(alumno.get_registro())