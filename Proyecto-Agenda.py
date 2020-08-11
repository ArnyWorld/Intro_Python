import os 
CARPETA = 'contactos/'  #Carpeta de contactos
EXTENSION = '.txt'

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre=nombre
        self.telefono = telefono
        self.categoria = categoria
        
def app():
    #Revisa si la carpeta existe o no
    crear_directorio()
    #Muestra el menú de opciones
    mostrar_menu()    
    #Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')    
        opcion=int(opcion)
        
        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = existe_contacto(nombre_anterior) 
    if existe:
        with open(CARPETA + nombre_anterior+EXTENSION,'w') as archivo:
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')        
            telefono_contacto = input('Agrega el nuevo teléfono:\r\n')
            categoria_contacto = input('Agrega la nueva categoría:\r\n')
            
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
 
            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Teléfono: '+contacto.telefono+'\r\n')
            archivo.write('Categoría: '+contacto.categoria+'\r\n')
            
            # Cerramos archivo
            archivo.close()
            
            #renombrar el nombre del archivo
            os.rename(CARPETA+nombre_anterior+EXTENSION,CARPETA+nombre_contacto+EXTENSION)
    
            #mostrar mensaje de éxito
            print('\r\n Contacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')
        
    
    
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto: \r\n')
    
    #revisar si el contacto ya existe
    existe = existe_contacto(nombre_contacto) 
    if not existe:
    
        with open(CARPETA + nombre_contacto+EXTENSION,'w') as archivo:
            #Resto de los campos
            telefono_contacto = input('Agrega el teléfono:\r\n')
            categoria_contacto = input('Categoria del contacto:\r\n')
            
            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            
    
            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Teléfono: '+contacto.telefono+'\r\n')
            archivo.write('Categoría: '+contacto.categoria+'\r\n')

            #Mostrando un mensaje de éxito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime el contenido
                print(linea.rstrip())
            #Imprime uns eparador de contactos
            print('\r\n')
  
def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                #Imprime el contenido
                print(linea.rstrip())
                #Imprime uns eparador de contactos
            print('\r\n')
    except IOError:
        print('El contacto no existe') 
    app()    
    
def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado correctamente')
    except IOError:
        print('El contacto no existe') 
    #reiniciar app
    app()    
    
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre+EXTENSION)


def mostrar_menu():
    print('====* Seleccione del Menú lo que desea realizar *====')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    #creando la carpeta
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/')
    
    
app()
