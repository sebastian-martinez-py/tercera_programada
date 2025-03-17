from Clases.lista_enlazada import ListaEnlazadaOrdenada

def agregar_persona(lista, persona):
    lista.insertar(persona)

def listar_personas(lista):
    lista.imprimir()

def buscar_por_edad(lista, edad):
    actual = lista._ListaEnlazadaOrdenada__head
    encontrado = False
    while actual:
        if actual.get_data().get_edad() == edad:
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron personas con esa edad.")

def buscar_por_nombre(lista, nombre):
    actual = lista._ListaEnlazadaOrdenada__head
    encontrado = False
    while actual:
        if nombre.lower() in actual.get_data().get_nombre().lower():
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron coincidencias.")

def buscar_por_apellido(lista, apellido):
    actual = lista._ListaEnlazadaOrdenada__head
    encontrado = False
    while actual:
        if apellido.lower() in actual.get_data().get_apellido1().lower() or apellido.lower() in actual.get_data().get_apellido2().lower():
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron coincidencias.")

def borrar_por_posicion(lista, posicion):
    if posicion == 0:
        if lista._ListaEnlazadaOrdenada__head:
            lista._ListaEnlazadaOrdenada__head = lista._ListaEnlazadaOrdenada__head.get_next()
            print("Elemento eliminado.")
        else:
            print("La lista está vacía.")
    else:
        actual = lista._ListaEnlazadaOrdenada__head
        for _ in range(posicion - 1):
            if actual.get_next():
                actual = actual.get_next()
            else:
                print("Posición fuera de rango")
                return
        if actual.get_next():
            actual.set_next(actual.get_next().get_next())
            print("Elemento eliminado.")
        else:
            print("Posición fuera de rango.")