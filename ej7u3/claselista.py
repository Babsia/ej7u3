from clasenodo import nodo
from clasepersonal import personal 
from clasedocente import docente
from claseinvestigador import investigador
from clasepersonalapoyo import Papoyo
from clasedocenteinvestigador import docenteinvestigador




class Lista:
    __comienzo=None
    __actual=None
    __tope=0
    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
    def insertarElemento(self, unaPersona: personal, pos: int):
        if not isinstance(pos, int) or pos < 0:
            raise IndexError("Indice invalido")

        unNodo = nodo(unaPersona)
        if pos == 0:
            unNodo.setSiguiente(self.__comienzo)
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        else:
            i = 1
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                i += 1
                aux = aux.getSiguiente()
            if i == pos:
                unNodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(unNodo)
            else:
                raise IndexError("Indice fuera de rango")
        
        self.__tope += 1
        
    def agregarElemento(self, unaPersona: personal):
        unNodo = nodo(unaPersona)
        
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__actual = self.__comienzo
        
        else:
            aux = self.__comienzo
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(unNodo)
        
        self.__tope += 1
    def __iter__(self):
        return self
    
    def __next__(self) -> personal:
        
        if self.__actual == None:
            self.__actual = self.__comienzo
            raise StopIteration
        
        else:
            unaPersona = self.__actual.getPersona()
            self.__actual = self.__actual.getSiguiente()
            return unaPersona
    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            personas = [unaPersona.toJSON() for unaPersona in self]
        )
        return d
    def ordenarPersonal(self):
        # La k conserva el primer nodo del ultimo par ordenado para saber si el ordenamiento ha terminado
        # La cota conserva el segundo nodo del ultimo par ordenado para saber si quedan nodos que ordenar en la iteracion actual
        # unNodo es el nodo que se esta ordenando actualmente
        
        
        if self.__comienzo != None:
            
            k = None
            cota = None
            
            while k != self.__comienzo:
                
                k = self.__comienzo
                unNodo = self.__comienzo
                while unNodo.getSiguiente() != cota:
                    

                    if unNodo.getSiguiente().getPersona().getnom() < unNodo.getPersona().getnom():
                        
                        unaPersona = unNodo.getPersona()
                        unNodo.setPersona(unNodo.getSiguiente().getPersona())
                        unNodo.getSiguiente().setPersona(unaPersona)
                        k = unNodo
                    
                    unNodo = unNodo.getSiguiente()
                

                cota = k.getSiguiente()
    def mostrarElemento(self,pos):
        if pos < 0 or self.__comienzo == None:
            raise IndexError("Indice invalido")
        
        else:
            i = 0
            aux = self.__comienzo
            while i < pos and aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                i += 1
            if i == pos:
                unaPersona = aux.getPersona()
                print(unaPersona)
            else:
                raise IndexError("Indice fuera de rango")
    def getListadoAgentesInvestigadores(self,carrera):
        self.ordenarPersonal()
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}\n".format("Cuil", "Apellido", "Nombre", "Categoria incentivos", "Importe extra")
        for unaPersona in self:
            if isinstance(unaPersona, docenteinvestigador) and unaPersona.getcarrera().lower() == carrera.lower():
                cadena += "{0:<20}{1:<20}{2:<20}{3:<20}{4:<20.2f}\n".format(unaPersona.getcuil(), unaPersona.getapellido(), unaPersona.getnom(), unaPersona.getcategoria(), unaPersona.getimporte())
        return cadena
    def contarDocentesInvestigadores(self,nombreAreaInvestigacion: str):
        contadorDocentesInvestigadores = 0
        contadorInvestigadores = 0
        for unaPersona in self:
            if isinstance(unaPersona, docenteinvestigador) and unaPersona.getarea().lower() == nombreAreaInvestigacion.lower():
                contadorDocentesInvestigadores += 1
            elif isinstance(unaPersona, investigador) and unaPersona.getarea().lower() == nombreAreaInvestigacion.lower():
                contadorInvestigadores += 1
        return (contadorDocentesInvestigadores, contadorInvestigadores)
    def getListadoPersonal(self):
        self.ordenarPersonal()
        cadena = "{0:<20}{1:<20}{2:<20}{3:<20}\n".format("Nombre", "Apellido", "Tipo de agente", "Sueldo")
        for unaPersona in self:
            cadena += "{0:<20}{1:<20}{2:<20}{3:<20}\n".format(unaPersona.getnom(), unaPersona.getapellido(), unaPersona.__class__.__name__, unaPersona.calculosueldo())
        return cadena
    def getListadoDocentesInvestigadores(self, categoria: str):
        cadena = "{0:<20}{1:<20}{2:<20}\n".format("Apellido", "Nombre", "Importe extra")
        total = 0
        for unaPersona in self:
            if isinstance(unaPersona, docenteinvestigador) and unaPersona.getcategoria().lower() == categoria.lower():
                cadena += "{0:<20}{1:<20}{2:<20}\n".format(unaPersona.getapellido(), unaPersona.getnom(), unaPersona.getimporte())
                total += unaPersona.getimporte()
        cadena += "Importe total en concepto de incentivos: {0:.2f}\n".format(total)
        return cadena
