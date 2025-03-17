from Clases.cola_prioridad import ColaPrioridad

def agregar_persona_cola(cola, persona):
    cola.insertar(persona)

def listar_personas_cola(cola):
    cola.imprimir()

def buscar_por_edad_cola(cola, edad):
    actual = cola._ColaPrioridad__head
    encontrado = False
    while actual:
        if actual.get_data().get_edad() == edad:
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron coincidencias.")

def buscar_por_nombre_cola(cola, nombre):
    actual = cola._ColaPrioridad__head
    encontrado = False
    while actual:
        if nombre.lower() in actual.get_data().get_nombre().lower():
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron coincidencias.")

def buscar_por_apellido_cola(cola, apellido):
    actual = cola._ColaPrioridad__head
    encontrado = False
    while actual:
        if apellido.lower() in actual.get_data().get_apellido1().lower() or apellido.lower() in actual.get_data().get_apellido2().lower():
            print(actual.get_data())
            encontrado = True
        actual = actual.get_next()
    if not encontrado:
        print("No se encontraron coincidencias.")

def borrar_por_posicion_cola(cola, posicion):
    if posicion == 0:
        if cola._ColaPrioridad__head:
            cola._ColaPrioridad__head = cola._ColaPrioridad__head.get_next()
            print("Elemento eliminado.")
        else:
            print("La cola está vacía.")
    else:
        actual = cola._ColaPrioridad__head
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
