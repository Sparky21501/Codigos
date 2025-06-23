personas = {
    1:{"nombre":"Esteban", "telefono":96463677, "rut":221575407},
    2:{"nombre":"Jose", "telefono":96872624, "rut":216784767},
}


'''
Programa que registre una nueva persona, borre personas, actualice personas y muestre personas
'''
def registrar():
    persona=str(input("Ingrese nombre: "))
    telefono=int(input("Ingrese su numero de telefono: "))
    if len(str(telefono)) != 9:
        print("Error")
        return
    rut=int(input("Ingrese su rut sin puntos ni guion: "))
    sig_id=max(personas.keys()) + 1
    personas[sig_id]={
        "nombre":persona,
        "telefono":int(telefono), 
        "rut":rut
    }
    print("Usuario agregado")
    
def borrar():
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    seleccion = int(input("Ingrese id a borrar: "))
    del personas[seleccion]

def mostrar():

    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

def actualizar():
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    seleccion2=int(input("Ingrese id a actualizar: "))
    persona=str(input("Ingrese nombre: "))
    telefono=input("Ingrese su numero de telefono: ")
    if not telefono.isdigit() or len(telefono) != 9:
        print("ERROR")
        return
    rut=int(input("Ingrese su rut sin puntos o guion: "))
    personas[seleccion2]={"nombre":persona, "telefono": telefono, "rut":rut}

while True:
    op=int(input('''Ingrese una opcion
                 1.- Registrar
                 2.- Mostrar
                 3.- Borrar
                 4.- Actualizar
                 5.- Salir
    '''))
    match op:
        case 1:
            registrar()
        case 2:
            mostrar()
        case 3:
            borrar()
        case 4:
            actualizar()
        case 5:
            print("saliendo...")
            break
        case _:
            print("Error opcion invalida")
    