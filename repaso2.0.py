'''
Sistema de Gestión de Estudiantes

Crear un programa que permita registrar y mantener información de estudiantes.
Se debe ingresar:
- Nombre: tipo string (solo letras)
- Edad: tipo int, entre 5 y 100 años
- RUT: debe tener 8 o 9 dígitos, sin puntos ni guion
- Curso: una letra (A, B, C, D)

Validar cada campo y tener un mantenedor completo.

Menú:
1.- Ingresar Estudiante
2.- Mostrar Estudiantes
3.- Actualizar Estudiante
4.- Borrar Estudiante
5.- Mostrar estadísticas (último ingresado y total de estudiantes)
6.- Salir

Usar funciones con argumentos para validar y organizar acciones.
'''

estudiantes = {
    1:{"nombre" : "esteban", "edad" : 18, "rut" : 221575407, "curso" : "A"},
    2:{"nombre" : "Sparky", "edad" : 20, "rut" : 232686518, "curso" : "B"}
}



def agregar():
    estudiante = input("Ingrese nombre del estudiante: ")
    edad = int(input("Ingrese edad del estudiante: "))
    rut = int(input("Ingrese rut del estudiante: "))
    if len(str(rut)) != 9:
        print("El Rut debe tener 9 caracteres")
        return
    curso = input("Ingrese curso del estudiante [A] [B] o [C]: ")
    if len(curso) != 1:
        print("Error, solo debe ingresar 1 digito")
        return
    agestudiantes = max(estudiantes.keys()) +1
    estudiantes[agestudiantes] = {
        "nombre" : estudiante,
        "edad" : edad,
        "rut" : rut,
        "curso" : curso
    }
    print(f"El estudiante {estudiante} fue agregado")

def mostrar():
    for ids, valor in estudiantes.items():
        print(f"ID:{ids}")
        for clave, key in valor.items():
            print(f"{clave} : {key}")

def actualizar():
    for ids, valor in estudiantes.items():
        print(f"ID:{ids}")
        for clave, key in valor.items():
            print(f"{clave} : {key}")
    actestudiantes = int(input("Seleccione ID de estudiante a actualizar: "))
    estudiante2 = input("Ingrese nuevo nombre: ")
    edad2 = int(input("Ingrese nueva edad del estudiante: "))
    rut2 = int(input("Ingresenuevo rut del estudiante: "))
    curso2 = input("Ingrese nuevo curso del estudiante: ")
    estudiantes[actestudiantes] = {"nombre" : estudiante2, "edad" : edad2, "rut" : rut2, "curso" : curso2}
    print("Estudiante actualizado")


def eliminar():
    for ids, valor in estudiantes.items():
        print(f"ID:{ids}")
        for clave, key in valor.items():
            print(f"{clave} : {key}")
    dell = int(input("Seleccione ID del estudiante que desea eliminar: "))
    del estudiantes[dell]
    print("Estudiante eliminado correctamente: ")

def estadisticas():
    id_final = max(estudiantes)
    ultimo_estudiante = estudiantes[id_final]
    print(f"el ultimo estudiante fue {ultimo_estudiante["nombre"]},")
    print(f"el total de estudiantes es de {len(estudiantes)}")


while True:
    try:
        opc = int(input('''Seleccione una opcion
                        1.- Ingresar Estudiante
                        2.- Mostrar Estudiantes
                        3.- Actualizar Estudiante
                        4.- Borrar Estudiante
                        5.- Mostrar estadísticas (último ingresado y total de estudiantes)
                        6.- Salir
                        Seleccione una opcion: '''))
        match opc:
                case 1:
                    agregar()
                case 2:
                    mostrar()
                case 3:
                    actualizar()
                case 4:
                    eliminar()
                case 5:
                    estadisticas()
                case 6:
                    print("👋 Saliendo del sistema.")
                    break
                case _:
                    print("❌ Opción inválida.")
    except Exception:
     print("❌ Solo debe ingresar un número válido.")
