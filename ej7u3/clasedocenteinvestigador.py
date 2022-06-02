from clasedocente import docente
from claseinvestigador import investigador
from abc import ABC
class docenteinvestigador(docente,investigador):
    __categoria=''
    __importe=0

    def __init__(self, cuil, apellido, nom, sueldo, antiguedad, carrera, cargo, catedra,area,tipo,categoria:str,importe:int):
        super().__init__(cuil=cuil, apellido=apellido, nom=nom, sueldo=sueldo, antiguedad=antiguedad, carrera=carrera, cargo=cargo, catedra=catedra,area=area,tipo=tipo)
        self.__categoria=categoria
        self.__importe=importe
    def getcategoria(self):
        return self.__categoria
    def getimporte(self):
        return self.__importe

    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["categoria"] = self.getcategoria()
        d["__atributos__"]["importe"] = self.getimporte()
        return d
    def getSueldo(self) -> float:
        sueldo = docente.getSueldo(self)
        sueldo += self.getImporteExtra()
        return sueldo

