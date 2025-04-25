# #-----------------------------------------------------------------------------------------------------------------------------------------------
# # Ejercicio 1: Calcular el total de una compra de productos farmacéuticos

# # Variables Definidad

# cant = 0
# total = 0
# op = 0

# # Cuantos productos llevará

# cant = int(input("Cuantos productos llevará? "))

# # Repetir por la cantidad de productos

# for i in range(1, cant +1):
#     print("¿Qué prducto llevara?")
#     print("1.- diazepam 9000$")
#     print("2.- ibuprofeno 5000$")
#     print("3.- paracetamol 3000$")
    
#     op = int(input("ingrese que producto/s llevara: 1, 2, 3: "))

#     if op == 1:
#         print("Usted lleva Diazepam ($9000)")
#         total = total + 9000
#     elif op == 2:
#         print("Usted lleva Ibuprofeno ($5000)")
#         total = total + 5000
#     elif op == 3:
#         print("Usted lleva Paracetamol ($3000)")
#         total = total + 3000
#     else:
#         print("Opción no válida, por favor elija 1, 2 o 3")
#         continue

    
    
# # Total

# print("el total es de", total, "$")
# print("el total mas iva es:", total * 1.19, "$")
# print("gracias por su compra")

# #-----------------------------------------------------------------------------------------------------------------------------------------------
# # calcular rango de edad

# edad=int(input("ingrese su edad"))
# if edad<12:
#     print("usted es menor de edad")
# elif edad>=12 and edad<18:
#     print("usted es un adolescente")
# else:
#     print("usted es un adulto")

##-----------------------------------------------------------------------------------------------------------------------------------------------
# Clave If, else  

# clave=2150
# ClaveUsario=int(input("ingrese su clave: "))

# if clave==ClaveUsario:
#     print("clave correcta")
# else:
#     print("clave incorrecta")

# Clave Repetir

# for i in range(3):
#     clave=2150
#     ClaveUsario=int(input("ingrese su clave: "))

#     if clave==ClaveUsario:
#         print("clave correcta")
#         break
#     else:
#         print("clave incorrecta")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# # Explicacion de While

# num=0

# while num<=5:
#     print(num)
#     num+=1

# import time
# num= 10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp = "no"
# while resp != "si":
#     resp=input("desea salir del programa? :")

# clave = 21501
# intentos = 3
# contraseña=int(input("ingrese contraseña: "))

# while clave != contraseña:
#     intentos -= 1
#     print("le quedan",intentos, " restantes")
#     print("error; Clave incorrecta")
#     contraseña=int(input("ingrese su contraseña: "))
#     if intentos == 1 :
#         break
        
# if clave == contraseña:

#  print("ingreso correctamente :3")
# else:
#    print("numero de intentos alcanzado perfil bloqueado")

##-----------------------------------------------------------------------------------------------------------------------------------------------
## spermercado con while

# cant = 0
# total = 0
# op = 0


# while op != 4:
#     print("¿Qué prducto llevara?")
#     print("1.- diazepam 9000$")
#     print("2.- ibuprofeno 5000$")
#     print("3.- paracetamol 3000$")
#     print("4.- desea salir?")

#     op=int(input("ingrese que producto/s llevara: 1, 2, 3, 4: "))

#     if op == 1:
#         print("Usted lleva Diazepam ($9000)")
#         total +=9000
#     elif op == 2:
#         print("Usted lleva Ibuprofeno ($5000)")
#         total +=5000
#     elif op == 3:
#         print("Usted lleva Paracetamol ($3000)")
#         total +=3000
#     else: 
#         print("ingrese un numero valido")
#     print(total)        


# print(f"el total es de {total} $" )
# print(f"el total mas iva es: {round(total * 1.19)} $")
# print("gracias por su compra")
  

##-----------------------------------------------------------------------------------------------------------------------------------------------

# num = 5

# while num != 0:
#     num=int(input("ingrese un numero (cero para salir): "))
#     if num % 2 == 0: 
#         print(f"el numero {num} es par ")
#     else:
#         print(f"el numero {num} es impar ")
        


