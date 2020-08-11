w = 8
x = 5       #tipo int
y = 10.1    #tipo float
z = False   #tipo bool
a = "Arni"  #tipo str
print(x)
print(y)
print(z)
print(a)

#print("El resultado es: " + w + x)   Error
#print("El resultado es: " + str(w + x))   Alternativa
print("El resultado es: ", w + x)   # Otra alternativa

#Manejo de cadenas
m = "Hola "
n = "Arni"
#la forma de concatenar cadenas es con el simbolo +
p = m + n
print(p)

#Manejo de bool
n1 = 5
n2 = 10
res = n1 < n2
print(res)

if n2 < n1:
    print("El n2 SI es menor")
else:
    print("El n2 NO es menor")