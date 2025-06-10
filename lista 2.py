
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


lista_productos = ["Tomate","Palta","Choripan"]
precios = [1000, 900, 500]
carrito = []

while True:
    opc = int(input('''Seleccione una opcion
                    1.- Ingresar producto a la tienda
                    2.- Comprar
                    3.- Crear boleta
                    4.- Salir
                            '''))
    match opc:
        case 1:
            producto = input("Ingrese producto a llevar : ")
            lista_productos.append(producto)
            print(f"Usted agrego {producto} a la tienda ")
            productoprecio = int(input("Ingrese precio del producto : "))
            precios.append(productoprecio)
        case 2:
            total = 0
            print("Seleccione producto que se llevara")
            for x in range(len(lista_productos)):
                print(x + 1, ".-", lista_productos[x], "$",precios[x])
            pro=int(input("Seleccione que quiere comprar : "))
            carrito.append(pro-1)
            print(f"Se agrego {pro} al carrito")
            print(carrito)
        case 3:
            for i in carrito:
                print(lista_productos[x], "-$",precios[x])
                total = total + precios [x]
            print("El Total de articulos es", len(carrito))
            print("Su total neto es ", total)
            print("Su total mas iva es ", total * 1.19 )
        case 4:
            print("Hasta luego gracias por su compra")
            break
        case _:
            print("Error, opcion invalida")
    
