
import json
from claselista import Lista
from clasepersonal import personal 
from clasedocente import docente
from claseinvestigador import investigador
from clasepersonalapoyo import Papoyo
from clasedocenteinvestigador import docenteinvestigador

class objectencoder:

    def decodificarDiccionario(self, d):
        retorno = None
        if "__class__" not in d:
            retorno = d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                unaColeccionPersonal = class_()
                personas = d["personas"]
                for i in range(len(personas)):
                    dPersona = personas[i]
                    class_name = dPersona["__class__"]
                    class_ = eval(class_name)
                    atributos = dPersona["__atributos__"]
                    unaPersona = class_(**atributos)
                    unaColeccionPersonal.agregarElemento(unaPersona)
            retorno = unaColeccionPersonal
        return retorno
    def guardarJSONArchivo(self, diccionario, nombreArchivo):
        archivo = open(nombreArchivo, "w", encoding="UTF-8")
        json.dump(diccionario, archivo, indent=4)
        archivo.close()
    def leerJSONArchivo(self, nombreArchivo):
        archivo = open(nombreArchivo, encoding="UTF-8")
        diccionario = json.load(archivo)
        archivo.close()
        return diccionario