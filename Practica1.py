nombres = []

while True:
    try:
        opc = int(input('''
                        Seleccione una opcion
                        1.- Agregar nombre
                        2.- Verificar si nombre esta en la lista
                        3.- Eliminar nombre
                        4.- Salir
                            '''))
        match opc:
            case 1:
                try:
                    nombre = input("Ingrese nombre a agregar : ")
                    nombres.append(nombre)
                    print(f"El nombre '{nombre}' fue agregado : ")
                except Exception:
                    print("Solo debe ingresar caracteres")
            case 2:
                try:
                    search = input("Ingrese nombre a buscar :")
                    if search in nombres:
                        print("El nombre esta en la lista")
                        cantidad = nombres.count(search)
                        print(f"El nombre {search} aparece {cantidad} en total")
                    else:
                        print("El nombre ingresado no esta en la lista")
                except Exception:
                    print("Solo debe ingresar caracteres")        
            case 3:
                try:
                    for x, nombre in enumerate (nombres):
                        print(x+ 1 , ".-", nombre)
                    dell = int(input("Que nombre desea eliminar (Ponga solo el numero del nombre) : ")) -1
                    nombres.pop(dell)
                    print("Nombre eliminado correctamente")
                except Exception:
                    print("Solo debe ingresar numeros")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo debe ingresar numero")

