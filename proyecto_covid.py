import matplotlib.pyplot as plt

def listadoDeComunas():  #Función para mostrar al usuario el listado de comunas
    nombreComunas = []
    codigoComunas = []
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines() #Creará una lista con cada línea separada por commas
        print("")
        print("***** Comunas de Chile *****\n")
        for i in lineas:
            linea = i.split(",")    #Separa líneas por commas
            listaUsuario = linea[2] + " -> " + "[" + linea[3] + "]" #Genera el menú al usuario
            print(listaUsuario)
            nombreComunas.append(linea[2])
            codigoComunas.append(linea[3])
    
    return nombreComunas, codigoComunas

def listadoDeRegiones():    #Función para mostrar al usuario el listado de regiones
    nombreRegiones = []
    regionesNoRepetidas = []
    codigoRegiones = []
    codigosNoRepetidos = []
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines() #Creará una lista con cada línea separada por commas
        for i in lineas:
            linea = i.split(",")
            nombreRegiones.append(linea[0]) #Crea una lista con las regiones del archivo
        for j in nombreRegiones:
            if j not in regionesNoRepetidas:
                regionesNoRepetidas.append(j)   #La lista se forma sin regiones repetidas
        for k in lineas:
            linea = k.split(",")
            codigoRegiones.append(linea[1]) #Crea una lista con los códigos de regiones del archivo
        for l in codigoRegiones:
            if l not in codigosNoRepetidos:
                codigosNoRepetidos.append(l)    #La lista se forma sin códigos de regiones repetidos
        print("")
        print("***** Regiones de Chile *****\n")
        for elemento in range(0, 17):
            listaUsuario2 = regionesNoRepetidas[elemento] + " -> " + "[" + codigosNoRepetidos[elemento] + "]"
            print(listaUsuario2)
        return regionesNoRepetidas, codigosNoRepetidos

print("***** Menú de selección *****")
print("(1) Filtrar comunas.")
print("(2) Filtrar regiones.")
print("(3) Mostrar región/comuna más contagiada.")
print("(4) Salir.")
filtro = input("Ingrese la opción según el número correspondiente: ")
while int(filtro) < 1 or int(filtro) > 4:
    print("Error en la selección. Favor ingrese la opción que se muestra en el menú.")
    filtro = input(">>> ")

if filtro == "1":
    listadoComunas = listadoDeComunas()
    busqueda = input("Ingrese (a) si desea buscar por el nombre de la comuna,\n o (b) si desea buscarla por código: ")
    while busqueda != "a" and busqueda != "b":
        print("Error en la selección de búsqueda. Ingrese nuevamente...")
        busqueda = input(">>> ")
    if busqueda == "a":
        nombreComuna = input("Ingrese el nombre de la comuna: ")
        while nombreComuna not in listadoComunas[0]:
            print("Comuna ingresada inválida.")
            nombreComuna = input("Ingrese el nombre de la comuna nuevamente: ")
    else:
        codigoComuna = input("Ingrese el código de la comuna: ")
        while not codigoComuna.isnumeric():
            print("Ingreso inválido.")
            codigoComuna = input("Ingrese el código de la comuna: ")
        while codigoComuna not in listadoComunas[1]:
            print("Código de comuna ingresada inválida.")
            codigoComuna = input("Ingrese el código de la comuna nuevamente: ")

elif filtro == "2":
    listadoRegiones = listadoDeRegiones()
    busqueda = input("Ingrese (a) si desea buscar por el nombre de la región,\n o (b) si desea buscarla por código: ")
    while busqueda != "a" and busqueda != "b":
        print("Error en la selección de búsqueda. Ingrese nuevamente...")
        busqueda = input(">>> ")
    if busqueda == "a":
        nombreRegion = input("Ingrese el nombre de la región: ")
        while nombreRegion not in listadoRegiones[0]:
            print("Región ingresada inválida.")
            nombreRegion = input("Ingrese el nombre de la región nuevamente: ")
    else:
        codigoRegion = input("Ingrese el código de la región: ")
        while not codigoRegion.isnumeric():
            print("Ingreso inválido.")
            codigoRegion = input("Ingrese el código de la región: ")
        while codigoRegion not in listadoRegiones[1]:
            print("Código de región ingresada inválida.")
            codigoRegion = input("Ingrese el código de la región nuevamente: ")
    