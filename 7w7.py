

comprador = {
    1: {"nombre" : "Sparky", "ticket" : "G", "code" : 123456}    
}


def ids_compradores():
        for ids, datos in comprador.items():
            print(f"ID: {ids}")
            for clave, valor in datos.items():
                print(f"{clave} : {valor}")


def comprar():
    nombre = input("Ingrese su nombre: ")

    entrada = input("Ingrese tipo de entrada General = (G) o Vip = (V): ")
    if len(entrada) != 1:
        print("Error solo debe ingresar 1 caracter")
        return
    codigo = (input("Ingrese codigo de confirmacion (max 6 caracteres y  3 numeros ): "))
    if len(codigo) != 9:
        print("Error")
        print("El codigo de confirmacion debe tener 9 caracteres")
        return
    if not codigo[6].isdigit():
        print("EL codigo debe tener almenos 3 numeros")
        return
    ag_entrada=max(comprador.keys()) +1
    comprador[ag_entrada] = {
        "nombre" : nombre,
        "ticket" : entrada,
        "code" : codigo
    }
    print(f"{nombre} a comprado con exito")


def consultar():
    ingnombre = input("Ingrese nombre del comprador: ").strip().lower() #.strip().lower() = ayuda a buscar el nombre sin importar si tiene o no mayusculas lo va a encontrar igual
    encontrado = False
    for compradores in comprador.values():
        if compradores["nombre"] == ingnombre:
            print("*************************")
            print(f"El comprador {ingnombre} existe")
            encontrado = True
            break
    if not encontrado:
        print("Nombre no encontrado") 


def cancelar():
    ids_compradores()
    dell_comprador = int(input("Ingrese ID de comprador a eliminar: "))
    del comprador[dell_comprador]
    print("Compra cancelada")


while True: 
        
        opc = int(input('''
                        1.- Comprar entrada.
                        2.- Consultar compradores.
                        3.- Cancelar compra.
                        4.- Salir.
                        :::::::::::::: '''))
        match opc:
            case 1:
                comprar()
            case 2:
                consultar()
            case 3:
                cancelar()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")          