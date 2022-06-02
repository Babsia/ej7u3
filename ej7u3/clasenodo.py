from clasepersonal import personal

class nodo:
    __dato=None
    __siguiente=None
    def __init__(self,nuevodato:personal):
        self.__dato=nuevodato
        self.__siguiente=None
    def setSiguiente(self,NuevoNodo):
        self.__siguiente=NuevoNodo
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__dato
    def setPersona(self,dato):
        self.__dato=dato
    def getPersona(self):
        return self.__dato