def app():
    #Crear un archivo open('nombreArchivo','privilegio')
    archivo = open('archivo.txt', 'w') #w es un privilegio de escritura, si el archivo no existe lo creara
    
    #Generar números en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea '+ str(i) + "\r\n")
    
    #Cerrar el archivo
    archivo.close()
    
app()