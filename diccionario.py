# diccionario = conjunto de pares de datos

# dic = {
#     "nombre":"Mel broks",
#     "numero": 964063677,
#     "casado": True,
#     123:98
# }

# print(dic)

# for key,value in dic.items(): 
#     print(key,value)


# dic["ciudad"] = "talca"

# for key, lol in dic.items():
#     print(key,lol)

# frutas = {
#     "sandia" : 3000,
#     "manzana" : 4000,
#     "naranja" : 1500
# }

# print(frutas)
# fruta = input("Ingrese una fruta : ")
# precio = int(input("Ingrese el precio : "))
# frutas[fruta]=precio
# print(frutas)


frutas = {
    "Peras" : 600,
    "Manzanas" : 350,
    "Sandia" : 1500,
    "Palta" : 2000
}

while True:
    opc =int(input('''
                   Seleccione una opcion
                   1.- Ingresar fruta y precio
                   2.- Actualizar precio
                   3.- Borrar fruta y precio
                   4.- mostrar todas las frutas y precios
                   5.- comprar
                   6.- salir
                   '''))
    
    match opc:
        case 1:
            print(frutas)
            fruta = input("Ingrese una fruta : ")
            precio = int(input("Ingrese el precio : "))
            frutas[fruta]=precio
            print(frutas)
        case 2:
            for key, precio in frutas.items():
                print(key,precio)
            fruta = input("ingrese nombre de la fruta : ")
            precio = int(input("Ingrese nuevo precio : "))
            frutas[fruta]=precio
        case 3:
            for key, precio in frutas.items():
                print(key,precio)
            dell = input("Seleccione la fruta a borrar : ")
            del frutas[dell]
            
        case 4:
            for key, precio in frutas.items():
                print(key,precio)
        case 5:
            print("Que desea comprar")
            for key, precio in frutas.items():
                print(key,precio)
        case 6:
            print("Saliendo")
            break
        case _:
            print("opcion invalida")