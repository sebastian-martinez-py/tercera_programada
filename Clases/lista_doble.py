class NodoDoble:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node


class ListaDobleEnlazadaOrdenada:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def insertar(self, persona):
        nuevo_nodo = NodoDoble(persona)
        if not self.__head:
            self.__head = self.__tail = nuevo_nodo
        elif self.__head.get_data().get_edad() >= persona.get_edad():
            nuevo_nodo.set_next(self.__head)
            self.__head.set_prev(nuevo_nodo)
            self.__head = nuevo_nodo
        else:
            actual = self.__head
            while actual.get_next() and actual.get_next().get_data().get_edad() < persona.get_edad():
                actual = actual.get_next()
            nuevo_nodo.set_next(actual.get_next())
            nuevo_nodo.set_prev(actual)
            if actual.get_next():
                actual.get_next().set_prev(nuevo_nodo)
            else:
                self.__tail = nuevo_nodo
            actual.set_next(nuevo_nodo)

    def imprimir(self):
        actual = self.__head
        while actual:
            print(actual.get_data())
            actual = actual.get_next()
