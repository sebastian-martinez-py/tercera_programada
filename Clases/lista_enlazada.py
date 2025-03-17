class Nodo:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class ListaEnlazadaOrdenada:
    def __init__(self):
        self.__head = None

    def insertar(self, persona):
        nuevo_nodo = Nodo(persona)
        if not self.__head or self.__head.get_data().get_edad() >= persona.get_edad():
            nuevo_nodo.set_next(self.__head)
            self.__head = nuevo_nodo
        else:
            actual = self.__head
            while actual.get_next() and actual.get_next().get_data().get_edad() < persona.get_edad():
                actual = actual.get_next()
            nuevo_nodo.set_next(actual.get_next())
            actual.set_next(nuevo_nodo)

    def imprimir(self):
        actual = self.__head
        while actual:
            print(actual.get_data())
            actual = actual.get_next()