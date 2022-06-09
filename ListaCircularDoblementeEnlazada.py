from Numero import Numero


class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarUltimo(self,numero):
        valor = Numero(numero)

        if self.primero is None:
            self.primero = self.ultimo = valor
        else:
            temp = self.ultimo
            self.ultimo = temp.siguiente = valor
            self.ultimo.anterior = temp
        self.unirNodos()

    def unirNodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def recorre(self):
        temp = self.primero
        print("")
        print("NUMEROS DE LA LISTA".center(31,"-"))
        while temp:
            print(f"{temp.numero}".center(5))
            temp = temp.siguiente
            if temp == self.primero:
                break
        print("".center(31,"-"))

    def buscar(self, numero):
        temp = self.primero
        while temp != None:
            if temp.numero == numero:
                print(" ")
                print("DATO ENCONTRADO ".center(50,"-"))
                return temp
            if temp.siguiente == self.primero:
                return -1
            temp = temp.siguiente



