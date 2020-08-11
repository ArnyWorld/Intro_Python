#Las condicionales nos permiten realizar una acción cuando se cumple cierta condición
edad = 15
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

experiencia = 3
if experiencia == 3:
    print('Tienes experiencia de 3 años')
else:
    print('No tienes la experiencia solicitada')
    
#negación    
nombre = "Ronaldo"
if nombre != "Arnaldo":
    print('No eres Arnaldo')
else:
    print('Si eres Arnaldo')
    

"""   
    nombre = "Ronaldo"
if not nombre == "Arnaldo":
    print('No eres Arnaldo')
else:
    print('Si eres Arnaldo')
"""

usuario_autenticado= True
if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

#Existen diferentes operadores que son utilizadas para realizar condiciones
"""
< menor
> mayor
<= menor igual
>= mayor igual
!= distinto
== igual
"""
    
#Condicionales Anidados
usuario_Admin = True
if usuario_autenticado:
    if usuario_Admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesión')
    
#elif  
ocupacion = 'Estudiante'
if ocupacion == 'Estudiante':
    print('Tienes 50% dedescuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% dedescuento')
else:
    print('Debes pagar el 100%')

#condicionales con operadores lógicos
"""
El operador AND dara una respuesta verdadera siempre y cuando 
las condiciones sean verdaderas
El operador OR dara una respuesta verdadera siempre y cuando 
exista al menos una condición verdadera
"""
usuario_autenticado = True
usuario_Admin = True

if usuario_autenticado and usuario_Admin:
    print('Administrador')
elif usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')