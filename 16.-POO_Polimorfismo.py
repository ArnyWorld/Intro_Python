#Una clase debe comenzar con una Mayúscula 
class Alumno:
    #Constructor
    def __init__(self, nombre, registro,sexo, semestre):
        """Por defecto los atributos son públicos, si se quiere 
        cambiar a privado la variable debe comenzar con doble barra baja (__nombreVariable)
        si se quiere manejar una variable protegida debe comenzar con una barra baja (_nombreVariable)
        """
        self.nombre = nombre
        self.registro = registro
        self.sexo = sexo
        self.semestre = semestre
            
    def mostrar_informacion(self):
        print(f'Nombre :{self.nombre}, Registro: {self.registro}, Sexo: {self.sexo}, Semestre: {self.semestre}')
#Intanciando la clase

#GETTERS Y SETTERS |||  Get = Obtener valor     Set = Asignar valor
    def get_registro(self):
        return self.registro
        
    def set_registro(self, registro):
        self.registro = registro


#Crear una clase hijo de Alumno
class Docente(Alumno):
    def __init__(self,nombre, registro,sexo, semestre, especialidad):
        super().__init__(nombre, registro, sexo, semestre)
        self.especialidad = especialidad
        
    #Agregar un método que solo exista en Docente
    def get_especialidad(self):
        return self.especialidad
    
    def mostrar_informacion(self):
            print(f'Nombre :{self.nombre}, Registro: {self.registro}, Sexo: {self.sexo}, Semestre: {self.semestre}, Especialidad: {self.especialidad}')
        
docente = Docente('Arni',187894,'Masculino', '6to Semestre', 'Desarrollador Web')
docente.mostrar_informacion()
especialidad = docente.get_especialidad()
print(especialidad)