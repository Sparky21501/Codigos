
juegos ={ 
    1: {"Nombre": "Xenoblade Chronicles",
       "Precio": 45990,
       "code": "XbCh2025"},
    2: {"Nombre": "Mario Party",
       "Precio": 35990,
       "code": "Mp2025"}
}

def mostrar_juegos(dict):

    for ids, datos in dict.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

def ingresa_juego(dict):
    nombre = input("Ingrese nombre del juego: ")
    precio = int(input("Ingrese Precio del juego: "))
    code = input("Ingrese el codigo del juego: ")

    dict[len(dict)+1] =  {"Nombre": nombre,
        "Precio": precio,
        "code": code}

def borrar_juego(dict):
    mostrar_juegos(dict)
    borrar = int(input("Ingrese cual quiere borrar: "))
    del dict[borrar]


def validar_code(code):
    Mayuscula = 0
    Minuscula = 0
    Numero = 0
    for palabra in code:
        if palabra.isupper():
            Mayuscula += 1
        if palabra.islower():
            Minuscula += 1
        if palabra.isdigit():
            Numero += 1
    if Mayuscula and Minuscula and Numero

while True:
    op = int(input('''
                        1.- mostrar
                        2.- agregar
                        3.- borrar
                        4.- salir
                        Seleccione una opcion: '''))
    match op:
        case 1:
            mostrar_juegos(juegos)
        case 2:
            ingresa_juego(juegos)
        case 3:
            borrar_juego(juegos)
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Error")



