# nombrelista = []

# milista = [1,2,3,4,5]

# for elemento in milista:
#     print(elemento)

# print(milista[2])

# milista.append(6)

# for elemento in milista:
#     print(elemento)

# # insertar texto

# milista.insert(3,"juan")
# for elemento in milista:
#   print(elemento)

# # eliminar elemento

# milista = [1,2,3,'juan',4,5]
# milista.remove("juan")

## ordenar

# milista = [1,2,3,'juan',4,5]
# milista.reverse()

# for elemento in milista:
#     print(elemento)
from os import system
system("cls")

lista_productos = []

while True:
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Mostrar todos los productos")
    print("4.- Salir")
    opc = int(input("> "))
    match opc:
        case 1:
            producto = input ("Ingrese producto: ")
            lista_productos.append(producto)
            print(f"el producto '{producto}' fue agregado correctamente")
            input("Presione enter para continuar")
            system("cls")
        case 2:
            print("productos")
            cont = 1
            for i in lista_productos:
                print(f"{cont}.- {i}")
                cont+=1

            aux = int(input("Cual desea eliminar: ")) -1
            lista_productos.pop(aux)
            input("Presione enter para continuar...")
            system("cls")

        case 3:
            print("Productos")
            cont = 1
            for i in lista_productos:
                print(f"{cont}.- {i}")
            input("Presione enter para continuar...")
            system("cls")

        case 4:
            break
        case _:
            print("Error")