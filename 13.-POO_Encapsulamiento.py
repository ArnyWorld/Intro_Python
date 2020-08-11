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



alumno = Alumno('Gary Nova','125456','Masculino','1er semestre')
alumno.registro = 123456; #Cuando el atributo es privado no se puede modificar el valor.
alumno.mostrar_informacion()

alumno2 = Alumno('Sarai Blanco','125987','Femenino','8vo semestre')
alumno2.registro = 987654; #Cuando el atributo es privado no se puede modificar el valor.
alumno2.mostrar_informacion()
