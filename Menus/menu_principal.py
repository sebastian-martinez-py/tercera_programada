from Menus.menu_enlazada import menu_lista_enlazada
from Menus.menu_doble import menu_lista_doble
from Menus.menu_cola import menu_cola


def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Lista Enlazada Ordenada")
        print("2. Lista Doblemente Enlazada Ordenada")
        print("3. Cola de Prioridad")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_lista_enlazada()
        elif opcion == "2":
            menu_lista_doble()
        elif opcion == "3":
            menu_cola()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")




menu_principal()
