from Funciones.funciones_doble import *
from Clases.lista_doble import ListaDobleEnlazadaOrdenada
from Clases.persona import Persona

def menu_lista_doble():
    lista = ListaDobleEnlazadaOrdenada()
    while True:
        print("\nMenú - Lista Doblemente Enlazada Ordenada")
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
            agregar_persona_doble(lista, persona)
            print("Persona agregada con éxito.")
        elif opcion == "2":
            listar_personas_doble(lista)
        elif opcion == "3":
            criterio = input("Buscar por (1) Edad, (2) Nombre, (3) Apellido: ")
            if criterio == "1":
                edad = int(input("Ingrese la edad: "))
                buscar_por_edad_doble(lista, edad)
            elif criterio == "2":
                nombre = input("Ingrese el nombre o parte de él: ")
                buscar_por_nombre_doble(lista, nombre)
            elif criterio == "3":
                apellido = input("Ingrese el apellido o parte de él: ")
                buscar_por_apellido_doble(lista, apellido)
        elif opcion == "4":
            posicion = int(input("Ingrese la posición a eliminar: "))
            borrar_por_posicion_doble(lista, posicion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
