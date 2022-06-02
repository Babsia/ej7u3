from clasedocenteinvestigador import docenteinvestigador
from clasepersonal import personal 
from clasedocente import docente
from claseinvestigador import investigador
from clasepersonalapoyo import Papoyo
from claselista import Lista
from objectencoder import objectencoder
import json
class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.opcion4,
            'e':self.opcion5,
            'f':self.opcion6,
            'g':self.opcion7,
            'h':self.salir
            }
        unencoder=objectencoder()
        d=unencoder.leerJSONArchivo('personal.json')
        self.__M=unencoder.decodificarDiccionario(d)
    

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        unobjen=objectencoder()
        diccionario=self.__M.toJSON()
        unobjen.guardarJSONArchivo(diccionario, "personal.json")
        print('Salir')
    def ingresarpersona(self):
        cuil=input('ingrese el cuil: ')
        nombre=input('ingrese el nombre: ')
        apellido=input('ingrese el apellido: ')
        sueldobasico=float(input('sueldo basico: '))
        antiguedad=int(input('antiguedad: '))
        tipo=input('ingrese el tipo: ').capitalize()
        if tipo in ["Docente", "Docente-Investigador"]:
            carrera = input("Ingrese la carrera: ")
            cargo = input('ingrese el cargo: ')
            catedra = input("Ingrese la catedra: ")
        
        if tipo in ["Investigador", "Docente-Investigador"]:
            areaInvestigacion = input("Ingrese el area de investigacion: ")
            tipoInvestigacion = input("Inrgese el tipo de investigacion: ")
        
        if tipo == "Docente-Investigador":
            categoriaIncentivos = input("Seleccione la categoria de incentivos: " )
            importeExtra = int(input("Ingrese el importe extra: "))

        
        if tipo == "Personal de apoyo":
            categoria = input("Ingrese la categoria, de 1 a 22: ")
            while not (1 <= categoria <= 22):
                categoria = input("Categoria invalida, ingrese un numero entre 21 y 22: " )
        if tipo == "Docente":
            unaPersona = docente(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
        
        elif tipo == "Investigador":
            unaPersona = investigador(cuil, apellido, nombre, sueldobasico, antiguedad, areaInvestigacion, tipoInvestigacion)
        
        elif tipo == "Docente-Investigador":
            unaPersona = docenteinvestigador(cuil, apellido, nombre, sueldobasico, antiguedad, areaInvestigacion, tipoInvestigacion, catedra, areaInvestigacion, tipoInvestigacion, categoriaIncentivos, importeExtra)
        
        elif tipo == "Personal de apoyo":
            unaPersona = Papoyo(cuil, apellido, nombre, sueldobasico, antiguedad, categoria)
        
        return unaPersona
      

    def opcion1(self):
        print("opcion a")
        insertado = False
        unaPersona = self.ingresarpersona()
        posicion = int(input("Ingrese la posicion en la que desea insertar el agente: "))
        while not insertado:
            try:
                self.__M.insertarElemento(unaPersona, posicion)
            except IndexError:
                posicion = input("[ERROR] La posicion ingresada no es valida, reintente: ")
            else:
                insertado = True
            print("Agente insertado")
        input('')
       
        
    def opcion2(self):
        print("opcion b")
        unpersonal=self.ingresarpersona()
        self.__M.agregarElemento(unpersonal)
    def opcion3(self):
        print ('opcion c')
        posicion = int(input("Ingrese la posicion del agente que desea mostrar: "))
        mostrado = False
        while not mostrado:
            try:
                self.__M.mostrarElemento(posicion)
            except IndexError:
                posicion = int(("[ERROR] La posicion ingresada no es valida, reintente: "))
            else:
                mostrado = True
        input('')
    def opcion4(self):
        print('opcion d')
        nombreCarrera = input("Ingrese el nombre de la carrera: ")
        print(self.__M.getListadoAgentesInvestigadores(nombreCarrera))
        input('')
       
    def opcion5(self):
        nombreAreaInvestigacion = input("Ingrese el area de investigacion: ")
        cantidades = self.__M.contarDocentesInvestigadores(nombreAreaInvestigacion)
        print("Hay {0} docentes investigadores y {1} investigadores en el area {2}".format(cantidades[0], cantidades[1], nombreAreaInvestigacion))
    def opcion6(self):
        print(self.__M.getListadoPersonal())
        input('')
    def opcion7(self):
        categoriaInvestigacion = input("Seleccione la categoria de investigacion [I, II, III, IV, V]").upper()
        print(self.__M.getListadoDocentesInvestigadores(categoriaInvestigacion))
        input('')