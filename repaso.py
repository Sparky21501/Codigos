'''
Crear gestion de vehiculos
Crear programa para un parking de autos
se debe ingresar
Marca, año, patente, Tipo

Marca: tipo string, se debe tipear la marca
año: tipo int , solo de 4 digitos enteros
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C= Camioneta, M= moto

Se deve validar cada aspecto y tener un mantenedor para 
todos los vehiculos motorizados

1.- Ingresar Vehiculo
2.- Mostrar Vehiculos
3.- Actualizar Vehiculo
4.- Borrar Vehiculo
5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
6.- Salir

Usar dunciones con argumentos para poder validar
y para poder llamar las acciones dentro del menu
'''


autos = {
    1:{"marca" : "Volkswagen", "año" : 1990, "patente" : "GKSB78", "tipo": "S"},
    2:{"marca" : "audi", "año" : 2020, "patente" : "GKSB78", "tipo": "E"}   
}


def agregar():
    
    print("***************************************************")
    print("Bienvenido a Garage Sparky's")
    agauto = input("Ingre Marca del vehiculo: ")
    agaño = int(input("Ingrese Año del vehiculo: "))
    if len(str(agaño)) != 4:
        print("Error")
        print("Solo puede tener 4 caracter maximo y minimo")
    agpatente = input('''Ingrese pantente
                    A considerar
                    tiene que tener 4 letras minusculas y 2 numeros
                    : ''')
    if len(agpatente) != 6: # len(Nombre de variable agregada) ayuda a poner un limite de caracteres
        print("Error")
        print("Solo puede tener 6 caracteres maximo y minimo")
        return
    if not agpatente[4].isdigit():
        print("Error los ultimos 2 caracteres no son numeros")
    agtipo = input('''Ingrese tipo de auto
                   -Electrico (E)
                   -Camioneta (C)
                   -Sudan (S)
                   -Moto (M) 
                    : 
                   ''')
    if len(agtipo) != 1:
        print("Error")
        print("solo debe ser una Letra")
        return
    ag_garage=max(autos.keys())+1 # con max(nombre del diccionario.keys()) +1 podemos agregar un ID al diccionario original
    autos[ag_garage] ={
        "marca" :agauto,
        "año" : agaño,
        "patente": agpatente,
        "tipo" : agtipo}
    print("Auto Agregado al garage")

def mostrar():
    print("****************************")
    print("Los siguientes autos estan en el garage")
    for ids, datos in autos.items():
        print(f"Auto n°{ids}")
        for clave, valor in datos.items():
            print(f"{clave} : {valor}")


def actualizar():
        print("****************************")
        print("Los siguientes autos estan en el garage")
        for ids, datos in autos.items():
            print(f"Auto n°{ids}")
            for clave, valor in datos.items():
                print(f"{clave} : {valor}")
        actautos = int(input("Ingrese id de auto a actualizar: "))
        marca = input("Ingrese Marca del auto: ")
        año = int(input("Ingrese año del auto"))
        patente = input("Ingrese patente del auto: ")
        tipo = input("Ingrese tipo del auto: ")
        if len(tipo) != 1:
            print("Error")
            print("solo debe ser una Letra")
            return
        else:
            print("****************")
            print("Auto actualizado")
            print("****************")
        autos[actautos] = {"marca" : marca, "año": año, "patente" : patente, "tipo" : tipo}

def borrar():
    try:
        for ids, datos in autos.items():
            print(f"Auto n°{ids}")
            for clave, valor in datos.items():
                print(f"{clave} : {valor}")
        eliminar = int(input("Seleccione ID de auto a eliminar"))
        del autos[eliminar]
        print("Auto eliminado")
    except Exception:
        print("Error :( )")
        print("Solo debe seleccionar numeros enteros de los que aparecen, en ese caso el ID del auto)") 

def estadisticas():
    print("*************************************")
    ultimo_id = max(autos) # max(nombre del diccionario) busca el id mas grande del diccionario 
    ultimo_auto = autos[ultimo_id]
    print(f"El ultimo auto ingresado fue {ultimo_auto['marca']} del año {ultimo_auto['año']}, con patente {ultimo_auto['patente']}, tipo {ultimo_auto['tipo']} ")
    print(f"El total de autos en el Garage son: {len(autos)}") # con {len(nombre del diccionario)} se puede ver el total de cosas que hay en el diccionario
    print("*************************************")

while True: 
    try:
        opc = int(input('''Seleccione una opcion
                        1.- Ingresar Vehiculo
                        2.- Mostrar Vehiculos
                        3.- Actualizar Vehiculo
                        4.- Borrar Vehiculo
                        5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
                        6.- Salir
                        :::::::::::::  '''))
        
        match opc:
            case 1:
                agregar()
            case 2: 
                mostrar()
            case 3: 
                actualizar()
            case 4:
                borrar()
            case 5:
                estadisticas ()
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Error :( )")
        print("Solo debe seleccionar numeros enteros de los que aparecen)")            
            