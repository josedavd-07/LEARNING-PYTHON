#if True:
    # si es verdadero se ejecuta el codigo

#if False:
    # si es falso no se ejecuta el codigo    
    

#..................................................................................................................................

#ejemplos 1

edad = 18

if edad >= 18:
    print("eres mayor de edad")
else:
    #print(" menor de edad")
    
#..................................................................................................................................
    
# ejemplo 2


 dinero_en_mi_tarjeta = 100000
 precio_del_producto = 80000
 
 if dinero_en_mi_tarjeta >= precio_del_producto:
        print("puedes comprar el producto")

 elif dinero_en_mi_tarjeta < precio_del_producto:
     print("no puedes comprar el producto")
     
 elif dinero_en_mi_tarjeta == precio_del_producto: 
     print("puedes comprar el producto")  
     
 elif dinero_en_mi_tarjeta != precio_del_producto:    
     print("no puedes comprar el producto")
      
 elif precio_del_producto > dinero_en_mi_tarjeta:   
     print("no puedes comprar el producto")
    
 elif precio_del_producto < dinero_en_mi_tarjeta:
     print("puedes comprar el producto")
     
 else:
     print("no tienes dinero para comprar este producto") 
     
     
             
    
#.....................................................................................................................................

#ejemplo 3

contraseña_almacenada = "carro12"
contraseña_escrita = "carro12"

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÒN...")
else: 
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")    
    
    
#..................................................................................................................................... 
#en este ejemplo utilizaremos elif para que el codigo sea mas eficiente y no se repita tanto
#ejemplo 4

ingreso_mensual = 1000000
gastos_mensuales = 800000
ahorro_mensual = 200000

if ingreso_mensual > gastos_mensuales:
    print("puedes ahorrar")
elif ingreso_mensual == gastos_mensuales:
    print("no puedes ahorrar")
    
elif ingreso_mensual < gastos_mensuales:
    print("no puedes ahorrar")
    
else:
    print("no tienes dinero")


#.....................................................................................................................................

#ejemplo 5

invitacion = cupo = "1"

if invitacion == cupo:
    print("puedes entrar")
elif invitacion != cupo:
    print("no puedes entrar")
    
else:
    print("no fuiste invitado , no puedes entrar")
    
#.....................................................................................................................................


# if anidados y else if (elif)
#ejemplo 6

ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamèrica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
    
else: 
    print("sos pobre")

#.....................................................................................................................................













    
    
    







































