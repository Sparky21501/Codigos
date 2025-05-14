
# def suma():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese un otro numero: "))
#     print("El resultado de la suma es", n1 + n2)

# def resta():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese un otro numero: "))
#     print("El resultado de la resta es", n1 - n2)

# def multiplicacion():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese un otro numero: "))
#     print("El resultado de la multiplicacion es", n1 * n2)

# def division():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese un otro numero: "))
#     print("El resultado de la division es", n1 / n2)

# def calcu():
#     while True:
#         op = int(input('''Seleccione su opcion
#                     1.- Suma
#                     2.- Resta
#                     3.- Multiplicacion
#                     4.- Division   
#                     5.- Salir
#                     '''))

#         match op:
#             case 1:
#                 print("Suma")
#                 suma()
#             case 2:
#                 print("Resta")
#                 resta()
#             case 3:
#                 print("Multiplicacion")
#                 multiplicacion()
#             case 4:
#                 print("Division")
#                 division()
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")


def votacion():
    candidato1 = input("Ingrese nombre del candidato 1: ")
    candidato2 = input("Ingrese nombre del candidato 2: ")

    vcandidato1 = 0
    vcandidato2 = 0
    votonulo = 0
    cantidad_votantes = int(input("Ingrese cantidad de votantes: "))

    for i in range (1, cantidad_votantes + 1 ):
        voto = input(f"#{i} Por quien votaras, ({candidato1}) // ({candidato2}) : ")
        if voto == candidato1:
            vcandidato1 += 1
            print(f"Votante #{i}, Voto por el candidato 1")
            print(f"Votos a Favor de {candidato1} = {vcandidato1}")
        elif voto == candidato2:
            vcandidato2 += 1
            print(f"Votante #{i}, Voto por el candidato 2")
            print(f"Votos a Favor de {candidato2} = {vcandidato2}")
        else:  
            votonulo +=1
            print("Voto invalido, se tomara como Nulo")


    print("Resultados Finales...")

    if vcandidato1 > vcandidato2:
        print(f"{candidato1} Gana las votaciones con {vcandidato1} Votos a favor")
        print(f"{candidato2} Obtuvo solo {vcandidato2} Votos a favor")
    elif vcandidato2 > vcandidato1:
        print(f"{candidato2} Gana las votaciones con {vcandidato2} Votos a favor")
        print(f"{candidato1} Obtuvo solo {vcandidato1} Votos a favor")
    else:
        print("Es un empate...")

    print(f"Cantidad de Votos Nulos {votonulo}")

def promedio():
    n1 = int(input("Ingrese su primera nota: "))
    n2 = int(input("Ingrese su segunda nota: "))
    n3 = int(input("Ingrese su tercera nota: "))
    n4 = int(input("Ingrese su cuarta nota: "))
    print("Su promedio final es", (n1 + n2 + n3 + n4) / 4)

def signo():
    dia = int(input("Ingrese el día de su nacimiento (1-31): "))
    mes = int(input("Ingrese el mes de su nacimiento (1-12): "))

    if mes == 3 and dia >= 21 or mes == 4 and dia <=19:
        print("Usted es Aries")
    elif  mes == 4 and dia >20 or mes == 5 and dia <=20:
        print("Usted es Tauro")
    elif  mes == 5 and dia >21 or mes == 6 and dia <=21:
        print("Usted es Geminis")
    elif  mes == 6 and dia >22 or mes == 7 and dia <=21:
        print("Usted es Cancer")
    elif  mes == 7 and dia >22 or mes == 8 and dia <=22:
        print("Usted es Leo")
    elif  mes == 8 and dia >23 or mes == 9 and dia <=22:
        print("Usted es Virgo")
    elif  mes == 9 and dia >23 or mes == 10 and dia <=22:
        print("Usted es Libra")
    elif  mes == 10 and dia >23 or mes == 11 and dia <=22:
        print("Usted es Escorpio")
    elif  mes == 11 and dia >23 or mes == 12 and dia <=22:
        print("Usted es Sagitario")
    elif  mes == 12 and dia >23 or mes == 1 and dia <=21:
        print("Usted es Capricornio")
    elif mes == 1 and dia >22 or mes == 2 and dia <=17:
        print("Usted es Acuario")
    elif mes == 2 and dia >18 or mes == 3 and dia <=19:
        print("usted es Piscis")

def tarea():
    while True:
        op = int(input('''Seleccione una opcion
                    1.- Votaciones
                    2.- Sacar Promedio
                    3.- Signo zodiacal
                    4.- Salir
                       '''))

        match op:
            case 1:
                print("Votaciones ")
                votacion()
            case 2:
                print("Promedio ")
                promedio()
            case 3:
                print("Signo ")
                signo()
            case 4:
                print("Saliendo...")
                break
tarea()
