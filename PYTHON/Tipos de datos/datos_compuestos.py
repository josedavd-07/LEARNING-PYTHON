#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"]

#creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto")

#esto es vàlido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy Dalto"
}

print(diccionario['altura'])

#.......................................................................................................................

# los datos compuestos son aquellos que nos permite tener datos simples o compuestos pero que podemos agrupar
#la lista es un conjunto de datos

# ahora veremos el primer tipo de dato que son las listas
# la funcion prin lo que harar sera imprimir todos los datos almacenados en la lista

lista = ["tomate" , "cebolla" , "pimenton" , "zanahoria" , "pollo"]  #esto se conoce como arrays que tiene varios datos 
#print(lista)

# ahora miraremos como pedirle a la funcion "print" que nos de dicho dato que le pedimos
#ejemplo 1  

list = ["jabon" , "limpido" , "suavisante de ropa" , "varsol"]
#print(list[0])

# las listas son modificables 
#ejemplo

list = ["jabon" , "limpido" , "suavisante de ropa" , "varsol"]
list [3] = "vanish"
#print(list[3])



# un arrays es un tipo de matris y arreglo
# ahora veremos la siguiente matris o arreglo llamado tuplas

# las tuplas es lo mismo que las listas pero en ves de usar "[]" usaremos los "()" , la diferencia es que las listas son 
# modificables se pueden modificar y cambiar su valor .
#encambio las tuplas no se puede modificar su valor.

# ahora veremos un ejemplo de tuplas

#ejemplo 2

tuple = ("carlos" , "juan" , "pedro" , "santiago")
#print(tuple[0])
  
  #ahora veremos un ejemplo de tuplas y miraremos que da error si la modificamos ya que las tuplas no se pueden modificar
  
#ejemplo 3

tuple = ["jabon" , "limpido" , "suavisante de ropa" , "varsol"]
tuple[3] = "vanish"
print(tuple[3])


# ahora veremos la funcion (set)
#la funcion set es un conjunto y los datos almacenados no tienen un orden fijo pueden cambiar de posicion y no pasa nada
# la diferencia de las tuple y las list es que se escriben con "{}" en ves de "()" para las tuplas y "[]" corchetes para la list

# ejemplo 4

conjunto = {"jabon" , "limpido" , "suavisante de ropa" , "varsol"}
 
# al igual que las tuplas el conjunto "set" no se pude modificar su valor pero si se puede redifinir la variable
#en un conjunto no puede haber datos repetidos esto lo que hace es que en el conjunto "set" elimine los datos repetidos
# en cambio en las listas o en las tuplas se mostrarian dos veces los datos  
#aca vemos que hay dos datos repetidos pero a la hora de imprimir los datos nos borrarra  el que se encuentre duplicado en el conjunto

conjunto = {"jabon" , "limpido" , "suavisante de ropa" , "varsol" , "jabon"} 
#print(conjunto)

#los conjunto "set" no se pueden llamar por su indice 
#ejemplo
conjunto = {"jabon" , "limpido" , "suavisante de ropa" }
#print(conjunto[0]) esto no se puede hacer porque los conjuntos no se pueden llamar por su indice 

#ejemplo 5

conjunto = {"jabon" , "limpido" , "suavisante de ropa" , "varsol"}
#print(conjunto) # esto nos dara el conjunto "set" tal cual como esta escrito

# ahora veremos la funcion "diccionario" = "dict" que es un tipo de dato compuesto que nos permite almacenar datos de una manera mas organizada
# los diccionarios se escriben con "{}" y dentro de los corchetes se escriben los datos que queremos almacenar 
# y se separan con ":" y se separan con "," 
# la estructura de dict es la siguiente  key : value y se separan con ":" y se separan con "," 
#"key" : "value" , la coma es si hay mas de un dato de lo contrario no e pone la coma
#ejemplo 6

dict = {
    "nombre" : "carlos" ,
    "apellido" : "perez" ,
    "edad" : 25 , 
    "estatura" : 1.75
    }
#print(dict["nombre"])
#print(["estatura"]+3)





























 
 















































  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  