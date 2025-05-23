

print("Bienvenido al delivery de sushi")

cuenta = 0
productos= 0
piroll = 0
otroll = 0
pulproll = 0
angroll = 0

def opciones():
    global producto, cuenta, productos, piroll, otroll, pulproll, angroll
    while True:
        producto =int(input('''Seleccione su pedido
        1.- Pikachu Roll $4500
        2.- Otaku Roll $5000
        3.- Pulpo Venenoso Roll $5200
        4.- Anguila Electrica Roll $4800
        5.- Salir
        '''))
        match producto:
            
            case 1:
                print(f"Usted lleva Pikachu Roll")
                cuenta += 45000
                productos += 1
                piroll = piroll + 1
            case 2:
                print("usted lleva Otaku Roll")
                cuenta += 50000
                productos += 1
                otroll = otroll + 1
            case 3:
                print("Usted lleva Pulpo Venenoso Roll")
                cuenta += 5200
                productos += 1
                pulproll = pulproll + 1
            case 4:
                print("Usted lleva Anguila Electrica Roll")
                cuenta += 4800
                productos += 1
                angroll = angroll + 1
            case 5:
                print("**************************************")
                print(f"Lleva ${cuenta}")
                print("Saliendo....")
                print("**************************************")
                break


def descuento():
    global desc, descuento1, descuentof
    desc = int(input("""posee un codigo de descuento
                     1.- Si
                     2.- No
                     """))
    if desc == 1:
        while True:
            descuento1 = (input('''Ingrese el codigo: '''))
            if descuento1 == "soyotaku":
                print("Se a aplicado un descuento del 10%")
                descuentof = cuenta * 0.90
                break
            elif descuento1 != "soyotaku":
                print("Ingrese codigo valido")
    elif desc == 2:
        descuentof = 0
        print("Saliendo...")
                    




            
            

def boleta():
    
    print("**************************************")

    print(f"Total Productos {productos}")

    print("**************************************")
    print(f"Pikachuroll: {piroll}")

    print(f"Otaku roll: {otroll}")

    print(f"Pulpo Venenoso roll: {pulproll}")

    print(f"Anguila Electrica Roll: {angroll}")

    print("**************************************")
    
    print(f"Total a pagar {cuenta}")
    print(f"Descuento por codigo {descuentof}")
    print(f"Total {cuenta}")

    print("**************************************")



while True:
    try:
        op = int(input('''Ingrese opcion
                    1.- Seleccione su pedido
                    2.- Descuento
                    3.- Boleta
                    4.- Salir
                    '''))
        match op:
            case 1:
                opciones()
            case 2:
                descuento()
            case 3:
                boleta()
            case 4:
                break
    except Exception:
        print("Solo numero valido")
