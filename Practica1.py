
# # Ejercicio #1
# nombres = ["pepe"]

# while True:
#     try:
#         opc = int(input('''
#                         Seleccione una opcion
#                         1.- Agregar nombre
#                         2.- Verificar si nombre esta en la lista
#                         3.- Eliminar nombre
#                         4.- Salir
#                             '''))
#         match opc:
#             case 1:
#                 try:
#                     nombre = input("Ingrese nombre a agregar : ")
#                     nombres.append(nombre)
#                     print(f"El nombre '{nombre}' fue agregado : ")
#                 except Exception:
#                     print("Solo debe ingresar caracteres")
#             case 2:
#                 try:
#                     search = input("Ingrese nombre a buscar :")
#                     if search in nombres:
#                         print("El nombre esta en la lista")
#                         cantidad = nombres.count(search)
#                         print(f"El nombre {search} aparece {cantidad} en total")
#                     else:
#                         print("El nombre ingresado no esta en la lista")
#                 except Exception:
#                     print("Solo debe ingresar caracteres")        
#             case 3:
#                 try:
#                     for x, nombre in enumerate (nombres):
#                         print(x+ 1 , ".-", nombre)
#                     dell = int(input("Que nombre desea eliminar (Ponga solo el numero del nombre) : ")) -1
#                     nombres.pop(dell)
#                     print("Nombre eliminado correctamente")
#                 except Exception:
#                     print("Solo debe ingresar numeros")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo debe ingresar numero")




estudiantes = [] 

while True:
    try:
        opc = int(input('''Ingrese una opcion
                        1. Agregar estudiante
                        2. Eliminar estudiante
                        3. Ver todos los estudiantes
                        4. Buscar por nota mínima
                        5. Promedio de notas
                        6. Salir
                        '''))
        match opc:
            case 1:
                nombre  = input("Ingrese nombre del estudiante: ")
                edad = int(input("Ingrese edad del estudiante: "))
                notafinal = float(input("Ingrese nota final del estudiante: "))
                estudiante = [nombre, edad, notafinal]
                estudiantes.append(estudiante)
            case 2:
                for x, estudiante in enumerate (estudiantes):
                    print(x+ 1, ".-", estudiante)
                dell = int(input("Que estudiante desea eliminar: ")) -1
                estudiantes.pop(dell)
                print("Estudiante eliminado correctamente...")
            case 3:
                for x, estudiante in enumerate (estudiantes):
                    print(x+ 1, ".-", estudiante)
            case 4:
                if estudiantes:
                    nota_minima = float(input("Buscar estudiantes con nota mayor  o igual a: "))
                    resultado = [est for est in estudiantes if est[2] >= nota_minima]
                    if resultado:
                        print("Resultado:", resultado)
                    else:
                        print("No hay estudiante con nota mayor o igual a ", nota_minima)
                else:
                    print("no hay estudiante registrado")
            case 5:
                    if estudiantes:
                        suma = sum(est[2] for est in estudiantes)
                        total_notas = len(estudiantes)
                        promedio = suma / total_notas
                        print(f"El promedio del curso es {promedio:.2f}")
                    else:
                        print("No se registro estudiante")
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo debe ingresar numero")