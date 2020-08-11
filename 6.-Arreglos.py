lenguajes = ['Python','Go','PHP','Java','C#']
print (lenguajes)

#obtener elementos específicos del arreglo, el indice comienza en 0
print(f'En este curso estamos aprendiendo {lenguajes[0]}')
#ordenar el arreglo alfabeticamente
lenguajes.sort()
print (lenguajes)

#Modificar valores existentes del arreglo
lenguajes[4] = 'C++'
print (lenguajes)

#Agregando elementos al arreglo
lenguajes.append('JavaScript')
print (lenguajes)

#eliminando elementos de un arreglo
del lenguajes[2]
print (lenguajes)
#eliminando el último elemento del arreglo
lenguajes.pop()
print (lenguajes)
#eliminando elementos específicos del arreglo
lenguajes.pop(0)
print (lenguajes)
#eliminar por el dato almacenado en el arreglo
lenguajes.remove('PHP')
print(lenguajes)

