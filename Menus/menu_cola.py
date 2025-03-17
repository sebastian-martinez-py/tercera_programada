from Funciones.funciones_cola import *
from Clases.cola_prioridad import ColaPrioridad
from Clases.persona import Persona


def menu_cola():
    cola = ColaPrioridad()
    while True:
        print("\nMenú - Cola de Prioridad")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Buscar persona")
        print("4. Borrar persona por posición")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido1 = input("Primer Apellido: ")
            apellido2 = input("Segundo Apellido: ")
            edad = int(input("Edad: "))
            persona = Persona(nombre, apellido1, apellido2, edad)
            agregar_persona_cola(cola, persona)
            print("Persona agregada con éxito.")
        elif opcion == "2":
            listar_personas_cola(cola)
        elif opcion == "3":
            criterio = input("Buscar por (1) Edad, (2) Nombre, (3) Apellido: ")
            if criterio == "1":
                edad = int(input("Ingrese la edad: "))
                buscar_por_edad_cola(cola, edad)
            elif criterio == "2":
                nombre = input("Ingrese el nombre o parte de él: ")
                buscar_por_nombre_cola(cola, nombre)
            elif criterio == "3":
                apellido = input("Ingrese el apellido o parte de él: ")
                buscar_por_apellido_cola(cola, apellido)
        elif opcion == "4":
            posicion = int(input("Ingrese la posición a eliminar: "))
            borrar_por_posicion_cola(cola, posicion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
