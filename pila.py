class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    class Pila:
        def __init__(self):
            self.cabeza = None 