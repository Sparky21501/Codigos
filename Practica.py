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
#     1.- La Florida 20%
#     2.- La pintana 30%
#     3.- Puente alto 25%
#     4.- San Joaquin 15%
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

# grupof=int(input("Ingrese su grupo familiar (numero entero usted incluido) : "))

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
#     print(f"{peleador2}: {hp2} HP ")
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

