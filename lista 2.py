
#       -5 -4 -3   -2 -1
# numeros = [1 ,2 ,215 ,4 ,5]
#        0  1  2    3  4

# print(numeros[-3])

# for numero in numeros:
#     print("numero", numero*5)
# while True:
#     print(numeros)

#     numeros.append(64)

#     print(numeros)

#     numeros.insert(3,100)

#     print(numeros)

# frutas = ["Manzana", "Mango", "Membrillo" ]

# for fruta in frutas:
#     print(fruta)

# nombres = []
# apellidos = []

# while True:
#     print('''
#           1.- Insertar nombre y apellido
#           2.- Mostrar nombres y apellidos
#           3.- Buscar nombre
#           4.- Salir
#           ''')
#     opc = int(input("Seleccione una opcion : "))
#     match opc:
#         case 1:
#             print("********************************")
#             nom = input("Ingrese su nombre : ")
#             ape = input ("Ingrese su apellido : ")
#             nombres.append(nom)
#             print(nombres)
#             apellidos.append(ape)
#             print(apellidos)
#         case 2:
#             # c = 0
#             # for x in nombres:
#             #     print(nombres[c], apellidos[c])
#             #     c += 1
#             for x in range(len(nombres)):
#                 print(nombres[x], apellidos[x])
#         case 3:
#             busc = input("Busque un nombre : ")
#             if busc in nombres:
#                 print(f"El nombre {busc} existe")
#             else:
#                 print(f"El nombre {busc} no existe")
#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Opcion invalida")


# lista_productos = ["Tomate","Palta","Choripan"]
# precios = [1000, 900, 500]
# carrito = []

# while True:
#     opc = int(input('''Seleccione una opcion
#                     1.- Ingresar producto a la tienda
#                     2.- Comprar
#                     3.- Crear boleta
#                     4.- Salir
#                             '''))
#     match opc:
#         case 1:
#             producto = input("Ingrese producto a llevar : ")
#             lista_productos.append(producto)
#             print(f"Usted agrego {producto} a la tienda ")
#             productoprecio = int(input("Ingrese precio del producto : "))
#             precios.append(productoprecio)
#         case 2:
#             total = 0
#             print("Seleccione producto que se llevara")
#             for x in range(len(lista_productos)):
#                 print(x + 1, ".-", lista_productos[x], "$",precios[x])
#             pro=int(input("Seleccione que quiere comprar : "))
#             carrito.append(pro-1)
#             print(f"Se agrego {pro} al carrito")
#             print(carrito)
#         case 3:
#             for i in carrito:
#                 print(lista_productos[x], "-$",precios[x])
#                 total = total + precios [x]
#             print("El Total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total * 1.19 )
#         case 4:
#             print("Hasta luego gracias por su compra")
#             break
#         case _:
#             print("Error, opcion invalida")



notas = [7.0, 4.6, 4.9, 7.0, 6.9]

while True:
    try:
        print('''
            1.- Ingresar nota
            2.- Borrar nota
            3.- Mostrar notas
            4.- Sacar promedio, nota mayor y nota menor
            5.- Limpiar todas las notas
            6.- Salir''')
        try:
            op=int(input("Seleccione una opcion : "))
        except Exception:
            print("Solo numeros sin decimales")
        match op:
            case 1:
                try:
                    nota = float(input("Ingrese una nota : "))
                    notas.append(nota)
                except Exception:
                    print("Solo debe ingresar numeros con decimal EJ: 6.0, 7.0")
            case 2:
                try:
                    for x, nota in enumerate(notas):
                        print(x+ 1,".-", nota)
                    eliminar = int(input("Que nota desea eliminar : ")) -1
                    notas.pop(eliminar)
                    print("Nota eliminada")
                except Exception:
                    print("Debe de ingresar numero de la nota, no la nota")
            case 3:
                print("Sus notas son")
                print(notas)
            case 4:
                suma = sum(notas)
                total_notas = len(notas)
                promedio = suma / total_notas
                print(f"Su promedio es {promedio} " )
                notas.sort()
                print("La nota mayor es ", notas [-1])
                print("La nota menor es ", notas [0])
            case 5:
                opc = int(input('''
                    Desea eliminar todas las notas
                    1.- Si
                    2.- No
                                '''))
                if opc == 1:
                    print("Borrando notas")
                    notas.clear()
                else:
                    print("Abortando...")
            case 6:
                print("Saliendo....")
                break   
            case _:
                print("Error, Opcion invalida")
    except Exception:
        print("Solo debe ingresar numero")
