from clasepersonal import personal

class docente(personal):
    # carrera en la que dicta clases, cargo y cátedra.
    __carrera=''
    __cargo=''
    __catedra=''
    def __init__(self,cuil,apellido,nom,sueldo,antiguedad,carrera,cargo,catedra,**kwargs):
        super().__init__(cuil,apellido,nom,sueldo,antiguedad,**kwargs)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def getcarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def getcatedra(self):
        return self.__catedra
    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["carrera"] = self.getcarrera()
        d["__atributos__"]["cargo"] = self.getcargo()
        d["__atributos__"]["catedra"] = self.getcatedra()
        return d
    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Carrera donde dicta clases:{}\nCargo:{}\nCatedra:{}\n".format(self.__carrera,self.__cargo,self.__catedra))
        return cadena
    def calculosueldo(self) -> float:
        sueldo = super().calculosueldo()
        if self.getcargo().lower() == "simple":
            sueldo += self.getsueldo() * 0.1
        elif self.getcargo().lower() == "semiexclusivo":
            sueldo += self.getsueldo() * 0.2
        elif self.getcargo().lower() == "exclusivo":
            sueldo += self.getsueldo() * 0.5
        return sueldo
    

    