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
    print("*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|")
    print("Bienvenido a Garage Sparky's")
    agauto = input("Ingre Marca del vehiculo: ")
    agaño = int(input("Ingrese Año del vehiculo: "))
    agpatente = input('''Ingrese pantenwe
                    A considerar
                    tiene que tener 4 letras minusculas y 2 numeros
                    : ''')
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
    ag_garage=max(autos.keys())+1
    autos[ag_garage] ={
        "Marca" :agauto,
        "año" : agaño,
        "patente": agpatente,
        "tipo" : agtipo}
    print("Auto Agregado al garage")


def mostrar():
    for ids, datos in autos.items():
        print("****************************")
        print("Los siguientes autos estan en el garage")
        print(f"Auto n°{ids}")
        for clave, valor in datos.items():
            print(f"{clave} : {valor}")


def actualizar():
    for ids, datos in autos.items():
        print("****************************")
        print("Los siguientes autos estan en el garage")
        print(f"Auto n°{ids}")
        for clave, valor in datos.items():
            print(f"{clave} : {valor}")
    seleccion = int(input("Seleccione Id a actualizar: "))
    marca = input("Ingrese marca del auto")
    año = int(input("Seleccione año del auto"))
    patente = input("Ingrese patente")
    tipo = ("Ingrese tipo del auto")

actualizar()