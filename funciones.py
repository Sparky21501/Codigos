# def suma():
#     n1 = int(input("Ingrese un numero"))
#     n2 = int(input("Ingrese un numero"))
#     print(n1+n2)

# def suma_ret():
#     n1 = int(input("Ingrese un numero"))
#     n2 = int(input("Ingrese un numero"))
#     return n1+n2

# def suma_arg(n1,n2):
#     print(n1+n2)

# def suma_arg_ret(n1, n2):
#     return n1+n2

# # suma()
# # num = suma_ret()
# # print(num*5)
# num1 = int(input("Ingrese un numero"))
# num2 = int(input("Ingrese un numero"))

# suma_arg(num1, num2)

# print("El resultado x2 es ",suma_arg_ret(num1, num2) *2)


# def iva():
#     total = int(input("Ingrese un valor total: "))
#     print("el total del valor con iva es: ",total*1.19)

# iva()


# def desc(descuento, precio):
#     return precio*(descuento/100)


# productos = [
#     {"nombre":"lapiz","precio":400},
#     {"nombre":"goma","precio":300},
#     {"nombre":"estuche","precio":1500}
# ]

# print(productos[2]["nombre"])

# for item in productos:
#     print(f"El articulo {item["nombre"]} tiene un precio de {item["precio"]}")



def mostrar_lista(lista):
    for x, producto in enumerate (lista):
        print(x+1, producto ["nombre"], producto ["precio"])

def insertar(lista):
    articulo = input("Ingrese nombre del articulo: ")
    precio = int(input("Ingrese Precio del articulo: "))
    lista.append({"nombre" : articulo, "precio" : precio})

def borrar_articulo(lista):
    mostrar_lista(lista)
    dell = int(input("Que articulo desea eliminar: ")) -1
    lista.pop(dell)

def actualizar():
    mostrar_lista(lista)
    act = int(input("cual producto desea actualizar"))
    articulo = (input("Seleccione el articulo: "))    
    precio = int(input("Agregue el nuevo precio: "))
    lista[articulo-1]["nombre"]=articulo 
    lista[articulo-1]["precio"]=precio

lista = [
    {"nombre":"papas","precio":300},
    {"nombre":"manzana","precio":500}
]
def menu(lista):
    while True:
        opc = int(input('''
                        1.- Agregar articulo
                        2.- Borrar articulo 
                        3.- Actualizar articulo
                        4.- Mostrar listado de lista
                        5.- Salir
                                Seleccione una opcion: '''))
        match opc:
            case 1:
                insertar(lista)
            case 2:
                borrar_articulo(lista)
            case 3:
                actualizar(lista)
            case 4:
                mostrar_lista(lista)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("opcion invalida")

menu(lista)