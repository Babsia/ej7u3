from menu import menuu
if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a Insertar a agentes a la colección. ")
        print("b Agregar agentes a la colección.")
        print("c Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print('d Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.')
        print('e  Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.')
        print('f Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.')
        print('g Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría,\n al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la \n categoría solicitada.  ')
        print ("h salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='h'
        