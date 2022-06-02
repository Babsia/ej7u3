from clasepersonal import personal
class investigador(personal):
    __area=''
    __tipo=''
    def __init__(self,cuil,apellido,nom,sueldo,antiguedad,area,tipo,**kwargs):
        super().__init__(cuil,apellido,nom,sueldo,antiguedad,**kwargs)
        self.__area=area
        self.__tipo=tipo
    def getarea(self):
        return self.__area
    def gettipo(self):
        return self.__tipo
    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["area"] = self.getarea()
        d["__atributos__"]["tipo"] = self.gettipo()
        return d
    def __str__(self):
        cadena =""
        cadena += super().__str__() + ("Area de investigacion: {}\nTipo de investigacion: {}".format(self.__area,self.__tipo))
        return cadena
    def calculosueldo(self):
        return super().calculosueldo()
        
        
    