from clasepersonal import personal
class Papoyo(personal):
    __categoria=''
    def __init__(self,cuil,apellido,nom,sueldo,antiguedad,categoria):
        super().__init__(cuil,apellido,nom,sueldo,antiguedad)
        self.__categoria=categoria
    def getcategoria(self):
        return self.__categoria
    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["categoria"] = self.getcategoria()
        return d
    def __str__(self):
        cadena = ""
        cadena += super().__str__() + ("Categoria:{}".format(self.__categoria))
        return cadena
    def calculosueldo(self) -> float:
        sueldo = super().calculosueldo()
        if 1 <= self.getcategoria() <= 10:
            sueldo += self.getsueldo() * 0.1
        elif 11 <= self.getcategoria() <= 20:
            sueldo += self.getSueldo() * 0.2
        elif 21 <= self.getcategoria() <= 22:
            sueldo += self.getsueldo() * 0.3
        return sueldo