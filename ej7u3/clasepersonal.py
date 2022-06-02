
from abc import ABC
import abc
class personal(ABC):
    #cuil, apellido, nombre, sueldo básico y antigüedad.
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldo=0
    __antiguedad=0
    def __init__(self,cuil:str,apellido:str,nom:str,sueldo:float,antiguedad:int,**kwargs):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nom
        self.__sueldo=sueldo
        self.__antiguedad=antiguedad
    def getcuil(self):
        return self.__cuil
    def getapellido(self):
        return self.__apellido
    def getnom(self):
        return self.__nombre
    @abc.abstractmethod
    def calculosueldo(self):
        sueldo = self.getsueldo() + self.getsueldo() * 0.01 * self.getant()
        return sueldo

    def getsueldo(self) -> float:
        return self.__sueldo
    def getant(self):
        return self.__antiguedad
    @abc.abstractmethod
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getcuil(),
                apellido = self.getapellido(),
                nom = self.getnom(),
                sueldo = self.getsueldo(),
                antiguedad = self.getant()                
            )
        )
        return d
    def __str__(self):
       return ("Apellido y Nombre:{} {}\n Cuil:{}\nSueldo Basico:${}\nAntiguedad\n".format(self.__apellido,self.__nombre,self.__cuil,self.__sueldo,self.__antiguedad))
