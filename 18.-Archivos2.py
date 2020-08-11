#Leyendo el contenido del archivo.txt
def app():
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())
        
app()