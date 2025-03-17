from Clases.lista_doble import ListaDobleEnlazadaOrdenada

def agregar_persona_doble(lista, persona):
    lista.insertar(persona)

def listar_personas_doble(lista):
    lista.imprimir()

def buscar_por_edad_doble(lista, edad):
    if not lista.get_head():
        print("Lista vacía")
        return
    if abs(lista.get_head().get_data().get_edad() - edad) <= abs(lista.get_tail().get_data().get_edad() - edad):
        actual = lista.get_head()
        while actual:
            if actual.get_data().get_edad() == edad:
                print(actual.get_data())
            actual = actual.get_next()
    else:
        actual = lista.get_tail()
        while actual:
            if actual.get_data().get_edad() == edad:
                print(actual.get_data())
            actual = actual.get_prev()

def buscar_por_nombre_doble(lista, nombre):
    actual = lista.get_head()
    while actual:
        if nombre.lower() in actual.get_data().get_nombre().lower():
            print(actual.get_data())
        actual = actual.get_next()

def buscar_por_apellido_doble(lista, apellido):
    actual = lista.get_head()
    while actual:
        if apellido.lower() in actual.get_data().get_apellido1().lower() or apellido.lower() in actual.get_data().get_apellido2().lower():
            print(actual.get_data())
        actual = actual.get_next()

def borrar_por_posicion_doble(lista, posicion):
    actual = lista.get_head()
    for _ in range(posicion):
        if actual.get_next():
            actual = actual.get_next()
        else:
            print("Posición fuera de rango")
            return
    if actual.get_prev():
        actual.get_prev().set_next(actual.get_next())
    if actual.get_next():
        actual.get_next().set_prev(actual.get_prev())
    if actual == lista.get_head():
        lista._ListaDobleEnlazadaOrdenada__head = actual.get_next()
    if actual == lista.get_tail():
        lista._ListaDobleEnlazadaOrdenada__tail = actual.get_prev()
    print("Elemento eliminado.")
