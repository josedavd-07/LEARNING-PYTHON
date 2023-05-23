# esto nos permitira entender las estructura de lo que veremos a continuacion

#Definiendo una variable con camelCase
nombreCompletoDeTuTioMaster = "Lucas Dalto"

#Definiendo una variable con snake_case
nombre_completo_de_tu_tio_master = "Lucas Dalto"


#concatenar con +
bienvenida = "Hola " + " ¿Como estas?"

#concatenar con f-strings
bienvenida = f"Hola {nombre_completo_de_tu_tio_master} ¿Como estas?"


#operadores de pertenencia (in / not in)
#print("Lucas" in bienvenida) #true
#print ("Lucas" not in bienvenida) #false

#...............................................................................


# Estas son variables que nos permiten almacenar datos en memoria para poder utilizarlos mas adelante en nuestro codigo 
a = 5
b = 10
c = a + b
#print (c)

# Ahora veremos como podemos asignarle un valor a una variable y luego imprimirlo en pantalla.

nombre = "Juan" 


#ejemplo 1

nombre = "Juan" 
#print (nombre)

 #ejemplo 2
 
numero = 10 + 5
#print (numero)

# ahora veremos como definir una variable con camel case que es cuando la primera palabra de la variable va en minuscula 
# y la segunda palabra va en mayuscula

nombreCompleto = "Juan Perez"

# ahora veremos como definir una variable con snake case que es cuando la primera palabra de la variable va en minuscula y separada con ( _ )
nombre_completo = "carlos"

# las variables se nombran y definen ejemplo  la variable la nombro :juguete y con el signo "=" le asigno un valor que en este caso es un string "carro"
#ejemplo 3

juguete = "carro"
#print (juguete)

#las variables se puden modificar porque ya estan declaradas y se les puede asignar otro valor ejemplo
#ejemplo 4
# en el siguiente ejercicio pudimos observar como la variable vehiculo se le asignaron 3 valores diferentes y el ultimo valor que se le asigno fue el 
# que se imprimio en pantalla

Vehiculo = "avion"
Vehiculo = "carro"
Vehiculo = "motocicleta"
#print (Vehiculo)
 
 #ejemplo 5
 
numero = 10
numero += 10
numero += 10
#print (numero)


# ahora veremos como concatenar variables y strings con el operabdor "+" 

bienvenida = " hola " + nombre + " ¿como estas?"

#ejemplo 6
# en el siguiente ejemplo se concateno la variable nombre con el string "hola" y el string "¿como estas?" y se guardo en la variable bienvenida
# y luego se imprimio en pantalla la variable bienvenida
#como pudimos observar como se concateno un string con una variable y otro string , pero para que no queden juntos 
# a los string se les agrego un espacio en blanco para que no queden juntos al momento de imprimirse en pantalla

nombre = "Juan"
bienvenida = " hola " + nombre + " ¿como estas?"
#print (bienvenida)

# ahora veremos como conctenar variables y strings con numeros con f strings 

bienvenida = f" hola {nombre} ¿como estas?"

#ejemplo 7
 # con los f string podemos pasar cualquier tipo de dato ya sea numero o booleano en texto
 
nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
#print (bienvenida)

# ahora veremos como hacer que una variable no este mas declaradapara esto usamos el operador "del" y el nombre de la variable que queremos eliminar
#ejemplo 8
# en el siguiente ejemplo se elimino la variable nombre y luego se imprimio en pantalla la variable nombre y nos dio un error porque 
# la variable nombre ya no existe porque fue eliminada con el operador "del" 

nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
del bienvenida
#print (bienvenida)

# si usamos utilimos el operador del antes dedefinir otra variable nos toma el valor inicial de la variable que eliminamos y si borramos el 
# valor inicial de la variable que eliminamos nos dara un error porque la variable ya no existe
#ejemplo 9
nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
del nombre
#print (bienvenida)

# ahora veremos operadores de pertenencia que son los operadores "in" y "not in" que nos sirven para saber si un valor esta dentro de una variable 

#print ("Juan" in "hola Juan ¿como estas?") #true juan si esta en hola juan ¿como estas?

#print ("carlos" in "hola Juan ¿como estas?") #false carlos no esta en hola juan ¿como estas?

#ejemplo 10

nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
#print ("Juan" in bienvenida)

#ahora veremos un ejemlo de como usar el operador "not in" que nos sirve para saber si un valor no esta dentro de una variable
#ejemplo 11
#como podemos ver depende el dato que les demos nos dara si esta o no esta si le damos carlos dara false porque no esta en la variable bienvenida 
# pero si le damos juan dara true porque si esta en la variable bienvenida

nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
#print ("carlos" not in bienvenida)

# ahora veremos que python es un lenguaje sensible a mayusculas y minusculas y que si no escribimos bien el nombre de la variable nos dara un error 
#aunque que escribamos bien el nombre de la variable pero con mayusculas y minusculas nos dara un error 
# porque python es un lenguaje sensible a mayusculas y minusculas
#ejemplo 12
# como podemos ver en el siguiente ejemplo se escribio bien el nombre de la variable pero con mayusculas y minusculas y nos dio un error
# porque python es un lenguaje sensible a mayusculas y minusculas

nombre = "Juan"
bienvenida = f" hola {nombre} ¿como estas?"
#print ( "Hola" in bienvenida)

#ahora veremos un metodo que nos permite dar formato a un string y este metodo es el metodo ".format" 

#ejemplo 13

nombre = "Juan"
bienvenida = " hola {} ¿como estas?".format(nombre)
#print (bienvenida) #la salida de este ejemplo es hola Juan ¿como estas? porque el metodo ".format" nos permite dar formato a un string 


nombre = "Juan"
edad = 25
#print("Hola, mi nombre es {} y tengo {} años").format(nombre, edad)
























































