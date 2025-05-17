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

##-----------------------------------------------------------------------------------------------------------------------------------------------


# impar=0
# par=0
# num=1

# while num!=0:
#     num=int(input("ingrese un numero 0.- para salir"))
#     if num % 2==0:
#         print(f"el numero es {num} es par")
#         par += 1
#     else:   
#         print(f"el numero {num} es impar")
#         impar +=  1
# print (f"hubo {par} pares y {impar} impares")
    
##-----------------------------------------------------------------------------------------------------------------------------------------------

# num =1 
# num =1 

# while num !=0:
#     num = int(input("ingrese un numero"))
#     if num != 0:
#         print(f"la suma de todos los numeros seria {num+0} ")
# while num !=0:
#     num = int(input("ingrese un numero"))
#     if num != 0:
#         print(f"la suma de todos los numeros seria {num+0} ")


##-----------------------------------------------------------------------------------------------------------------------------------------------

# import random

# numazar = random.randint(1,30)

# print(numazar)

# if numazar >= 20:
#     print("puede pasar")
# else:
#     print("Le falta puntaje")

# import random

# numazar = random.randint (1,50)
# adivinar=int(input("Adivine el numero"))

# while adivinar != numazar:

#     if adivinar>numazar:
#         print("el numero es menor")
#         adivinar=int(input("Adivine el numero"))

#     if adivinar<numazar:
#         print("el numero es mayor")
#         adivinar=int(input("Adivine el numero"))
# else: adivinar == numazar
# print("adivino el numero")


##-----------------------------------------------------------------------------------------------------------------------------------------------
    
# import time
# import random

# j1 = 0
# j2 = 0
# meta = 30
# turno = 0

# while j1 < meta and j2 < meta:
#     turno += 1
#     if turno % 2 == 0:
#         print("Turno de J1")
#         time.sleep(1)
#         dado = random.randint (1,6)
#         j1 = j1 + dado
#         print(f"El j1 saco {dado}")
#         print(f"Avanza hasta la casilla {j1}")
#     else:
#         print("turno de j2")
#         time.sleep(1)   
#         dado = random.randint (1,6)
#         j2 = j2 + dado
#         print(f"El j2 saco {dado}")
#         print (f"avanza hasta la casilla {j2}") 

# if j1 >=meta:
#     print("El ganador es j1")
# else:
#     print("El ganador es j2")




##-----------------------------------------------------------------------------------------------------------------------------------------------        

# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento

# arancel=200000
# descuento=0

# print('''
#     1.- La Florida 
#     2.- La pintana 
#     3.- Puente alto 
#     4.- San Joaquin 
# ''')
# comuna=int(input("Seleccione una comuna:"))

# if comuna == 1:
#     descuento = 20
# elif comuna == 2:
#     descuento = 30
# elif comuna == 3:
#     descuento = 25
# elif comuna == 4:
#     descuento = 15
# else:
#     print("Seleccione una opcion valida")

# grupof=int(input("Ingrese su grupo familiar contandose: "))

# if grupof == 1:
#     descuento += 2
# elif grupof <= 4 and grupof >= 2:
#     descuento += 3
# elif grupof >= 5:
#     descuento += 4
# else: 
#     print("Seleccione una opcion valida")

# print(f"el descuento total es {descuento}")
# desc = arancel*descuento/100
# total = arancel - desc
# print(f"El total a pagar es ${total}")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# STREET FIGTHER #

# Designe 2 peleadores solicitando sus nombres
# cada peleador tiene 50 HP, debe mostrar la 
# barra de energia. Las peleas son por turnos #print("[]"*20)
# cada turno el peleador ataca entre 3 y 15
# Existe posibilidad de ataque critico del 20% sera atk*2
# gana el que le quita todo el HP al rival

# import random
# import time


# peleador1 = input("Nombre del primer peleador: ")
# peleador2 = input("Nombre del segundo peleador: ")

# hp1 = 50
# hp2 = 50

# turno = 0
# while hp1 > 0 and hp2 > 0:
#     print(f"turno {turno}")
#     if turno % 2 != 0:
#         atacante = peleador1
#         defensor = peleador2
#         hp_defensor = hp2
#     else: 
#         atacante = peleador2
#         defensor = peleador1
#         hp_defensor = hp1  

#     daño = random.randint(3, 15)
#     critico = random.random() < 0.2
#     if critico:
#         daño *= 2
#         print ("a dado un golpe critico")

#     hp_defensor -= daño
#     if turno % 2 != 0:
#         hp2 = max(hp_defensor, 0)
#     else:
#         hp1 = max(hp_defensor, 0)

#     print(f"{peleador1}: {hp1} HP ")
#     print("▄"*hp1)
#     print(f"{peleador2}: {hp2} HP ")
#     print("▄"*hp2)

#     turno += 1
#     time.sleep(2)

# if hp1 <= 0:
#     print (f"gana {peleador2}")
# else:
#     print (f"gana {peleador1}")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quin votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate

# candidato1 = input("Primer candidato: ")
# candidato2 = input("Segundo candidato: ")

# cantv = int(input("Ingrese la cantidad de votantes: "))

# vcandidato1 = 0
# vcandidato2 = 0

# for i in range (1, cantv + 1):
#     voto = input(f"Votante #{i}, Por quien votaras: ({candidato1}) / ({candidato2}): ")
#     if voto == candidato1:
#         vcandidato1 +=1
#     elif voto == candidato2:
#         vcandidato2 +=1
#     else:
#         print("Voto invalido. no se contara")

# print("Resultados de la votacion")
# print(f"{candidato1} obtuvo {vcandidato1} votos ")
# print(f"{candidato2} obtuvo {vcandidato2} votos ")

# if vcandidato1 > vcandidato2:
#     print(f"{candidato1} Gana con: {vcandidato1} votos ")
# elif vcandidato2 > vcandidato1:
#     print(f"{candidato2} Gana con: {vcandidato2} votos ")
# else:
#     print("Es un empate")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# Pedir dia y mes de nacimiento y mostrar el signo zodiacal

# dia = int(input("Ingrese el día de su nacimiento (1-31): "))
# mes = int(input("Ingrese el mes de su nacimiento (1-12): "))

# if mes == 3 and dia >= 21 or mes == 4 and dia <=19:
#     print("Usted es Aries")
# elif  mes == 4 and dia >20 or mes == 5 and dia <=20:
#     print("Usted es Tauro")
# elif  mes == 5 and dia >21 or mes == 6 and dia <=21:
#     print("Usted es Geminis")
# elif  mes == 6 and dia >22 or mes == 7 and dia <=21:
#     print("Usted es Cancer")
# elif  mes == 7 and dia >22 or mes == 8 and dia <=22:
#     print("Usted es Leo")
# elif  mes == 8 and dia >23 or mes == 9 and dia <=22:
#     print("Usted es Virgo")
# elif  mes == 9 and dia >23 or mes == 10 and dia <=22:
#     print("Usted es Libra")
# elif  mes == 10 and dia >23 or mes == 11 and dia <=22:
#     print("Usted es Escorpio")
# elif  mes == 11 and dia >23 or mes == 12 and dia <=22:
#     print("Usted es Sagitario")
# elif  mes == 12 and dia >23 or mes == 1 and dia <=21:
#     print("Usted es Capricornio")
# elif mes == 1 and dia >22 or mes == 2 and dia <=17:
#     print("Usted es Acuario")
# elif mes == 2 and dia >18 or mes == 3 and dia <=19:
#     print("usted es Piscis")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# chocolate = 1

# if chocolate == 1:
#     print("Hay Chocolate ")
# else:
#     print("No Hay Chocolate ")


# gta6 = 0

# print("Salio GTA6 1.- Si, 0.- No ")
# gta6=int(input())

# if gta6 == 1:
#     print("Se puede jugar")
# else: 
#     print("No se puede jugar")


##-----------------------------------------------------------------------------------------------------------------------------------------------


# credito =0

# print("Calcule su porcentaje de credito: ")

# cantidad_de_ingreso = int(input('''
#         Seleccione sus ingresos
#  1.- 500.000 a 1.000.000
#  2.- 1.000.000 a 1.500.000 
#  3.- 1.500.001 o mas
# '''))

# if cantidad_de_ingreso == 1:
#     credito += 300000
#     print(f"Usted tiene ${credito} de credito ")
# elif cantidad_de_ingreso == 2:
#     credito += 650000
#     print(f"Usted tiene ${credito} de credito ")
# elif cantidad_de_ingreso == 3:
#     credito += 1000000
#     print(f"Usted tiene ${credito} de credito ")
# else:
#     print("Opcion invalida")


# nivel_educacional = int(input('''
#       Seleccione su nivel educacional                     
# 1.- Basico
# 2.- Medio
# 3.- Superior                                                           
# '''))

# if nivel_educacional == 1:
#     credito *= 1
#     print(f"Su credito por el nivel educacional Basico es = ${credito} ")
# elif nivel_educacional == 2:
#     credito *= 1.3
#     print(f"Su credito por el nivel educacional Medio es = ${credito} ")
# elif nivel_educacional == 3:
#     credito *= 1.5
#     print(f"Su credito por el nivel educacional Superior es = ${credito} ")
# else:
#     print("Opcion Invalida")

# nacionalidad = int(input('''
#         Seleccione su nacionalidad
# 1.- Chilena
# 2.- Extranjero
# '''))

# if nacionalidad == 1:
#     credito += 300000
#     print(f"Su credito total es ${credito}")
# elif nacionalidad == 2:
#     print(f"Su Credito total es ${credito} ")
# else:
#    print("opcion invalida")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# import random
# import colorama
# from colorama import Fore

# num1 = int(input("Seleccione un numero: "))
# num2 = int(input("Seleccione un segundo numero mayor al anterior: "))

# if num1 > num2:
#     print("El segundo numero no puede ser menor")
# else:
#     nrandom = random.randint(num1,num2) # colocar parentesis pegado al randint sino, no funcina y sin ningun igual
#     for i in range (nrandom):
#         print(Fore.BLUE, "▄")

# print(Fore.WHITE, f"Su numero random fue: {nrandom}")

##-----------------------------------------------------------------------------------------------------------------------------------------------   
# Clasificar segun categoria y precio
# Cat 1 +200, cat 2 +400, cat 3 +600
# Decuento Precios : 1000 y menos;3%, entre 1001 y 5000 
# ;5% , 5001 y mas 6%
# Poner listado de 3 productos por categoria, las cat son 1 ,2 y 3
# Agregar los impuestos al ´precio , segun la cat y luego 
# aplicar descuento al total de la boleta segun el monto
'''
Ej:
Producto 1, cat 2, 1500 + 400
Producto 2 cat 1, 8000 + 200
EL total es 10100 * - 6%
EL total a pagar es: 9494
'''

# preciofinal = 0

# print("------------------------")
# producto1 = int(input('''
# Eliga un porducto: 
# 1.- Mouse Logitech 5990$ + 200$
# 2.- Mouse Razer 2990$ + 400$
# 3.- Mouse Generico 1590$ + 600$
#  '''))
# print("------------------------")

# if producto1 == 1:
#     preciofinal += 6990 + 200
#     print("Usted lleva un mouse Logitech")
# elif producto1 == 2:
#     preciofinal += 3990 + 400
#     print("Usted lleva un mouse Razer")
# elif producto1 == 3:
#     preciofinal += 1590 + 600
#     print("Usted lleva un mouse Generico")
# else: 
#     print("Opcion invalida")

# print(f"Lleva {preciofinal}$")

# print("------------------------")
# producto2 = int(input('''
# Eliga otro producto: 
# 1.- Teclado RedDragon 4190$ + 200$
# 2.- Teclado Razer 4840$ + 400$
# 3.- Teclado Logitech 3290 + 600$
#  '''))

# if producto2 == 1:
#     preciofinal += 4190 + 200
#     print("Usted lleva un Teclado RedDragon")
# elif producto2 == 2:
#     preciofinal += 4840 + 400
#     print("Usted lleva un Teclado Razer")
# elif producto2 ==3:
#     preciofinal += 3290 + 600
#     print("Usted lleva un Teclado Logitech")
# else:
#     print("Opcion invalida")

# print(f"Lleva {preciofinal}$") 

# print("------------------------")
# producto3 = int(input('''
# Seleccione un ultimo producto: 
# 1.- Monitor 300hz 10990$ + 200
# 2.- Monitor 240hz 3990$ + 400
# 3.- Monitor 120hz 1490$ + 600
#  '''))

# if producto3 == 1:
#     preciofinal += 10990 + 200
#     print("Usted lleva un Monitor 300hz ") 
# elif producto3 == 2:
#     preciofinal += 3990 + 400
#     print("Usted lleva un Monitor 240hz")
# elif producto3 == 2:
#     preciofinal += 1490 + 600
#     print("Usted lleva un Monitor 120hz")
# else:
#     print("Seleccione una opcion valida")

# print(f"Lleva {preciofinal}")

# print("------------------------")
# preciofinal = preciofinal * 0.6 
# print(f"El total a pagar es {preciofinal}" )
# print("------------------------")

##-----------------------------------------------------------------------------------------------------------------------------------------------

# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quin votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate

# candidato1 = input("Ingrese nombre del candidato 1: ")
# candidato2 = input("Ingrese nombre del candidato 2: ")

# vcandidato1 = 0
# vcandidato2 = 0
# votonulo = 0
# cantidad_votantes = int(input("Ingrese cantidad de votantes: "))

# for i in range (1, cantidad_votantes + 1 ):
#     voto = input(f"#{i} Por quien votaras, ({candidato1}) // ({candidato2}) : ")
#     if voto == candidato1:
#         vcandidato1 += 1
#         print(f"Votante #{i}, Voto por el candidato 1")
#         print(f"Votos a Favor de {candidato1} = {vcandidato1}")
#     elif voto == candidato2:
#         vcandidato2 += 1
#         print(f"Votante #{i}, Voto por el candidato 2")
#         print(f"Votos a Favor de {candidato2} = {vcandidato2}")
#     else:  
#         votonulo +=1
#         print("Voto invalido, se tomara como Nulo")


# print("Resultados Finales...")

# if vcandidato1 > vcandidato2:
#     print(f"{candidato1} Gana las votaciones con {vcandidato1} Votos a favor")
#     print(f"{candidato2} Obtuvo solo {vcandidato2} Votos a favor")
# elif vcandidato2 > vcandidato1:
#     print(f"{candidato2} Gana las votaciones con {vcandidato2} Votos a favor")
#     print(f"{candidato1} Obtuvo solo {vcandidato1} Votos a favor")
# else:
#     print("Es un empate...")

# print(f"Cantidad de Votos Nulos {votonulo}")

##-----------------------------------------------------------------------------------------------------------------------------------------------

