numero = 0
while numero <10:
    if numero == 5:
        break   # permite forzar a que se detenga la ejecución 
    else:
        print(numero)
    numero += 1
    
    #ejercicio
    
    playlist = {}
    playlist['canciones']=[]
    
    def app():
        #Agregando Playlist
        agregar_playlist = True
        while agregar_playlist:
            nombre_playlist = input('¿Cómo deseas nombrar la playlist?\r\n')
            if nombre_playlist:
                playlist['nombre'] = nombre_playlist
                #ya se tiene un nombre, desactivar la lectura
                agregar_playlist = False
                agregar_canciones()

    def agregar_canciones():
        #bandera para agregar canciones
        agregar_cancion = True
        
        while agregar_cancion:
            #preguntar al usuario que canción desean agregar
            nombre_playlist = playlist['nombre']
            pregunta = f'Agrega canciones para la playlist {nombre_playlist} : \r\n' 
            pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'
            
            cancion = input(pregunta)
            if cancion == 'x':
                agregar_cancion = False
                #mostrar resumen
                mostrar_resumen()
            else:
                #dejar de agregar canciones
                playlist['canciones'].append(cancion)
                
    def mostrar_resumen():
        nombre_playlist = playlist['nombre']
        print(f'Playlist: {nombre_playlist} \r\n')
        print('Canciones: \r\n')
        for cancion in playlist['canciones']:
            print(cancion)
            
app()