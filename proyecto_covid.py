import matplotlib.pyplot as plt #importamos la libreria de graficos

def filtrarUltimasFechas(): #Función para alistar las últimas 7 fechas requeridas
    with open("Datos.csv", "r", encoding="utf-8") as file:  #abrirá el archivo, encriptando a utf-8
        ultimasFechas = []  #Se almacenarán las fechas seleccionadas a esta lista
        for i in file.readlines():
            linea = i.split(",")
            for j in range(len(linea)-8, len(linea)-1,1):      #El for ayudará a recorrer la lista de derecha a izquierda
                ultimasFechas.append(linea[j])                 #desde la última posición hasta la requerida (7) y luego
            break                                              #las almacenará a una lista vacía.
        return ultimasFechas

#------------------------------------------------------------------------------------------------------------------
#-----------------------------------------      COMUNAS      ------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

def listadoDeComunas():  #Función para mostrar al usuario el listado de comunas y sus códigos respectivamente
    nombreComunas = []
    codigoComunas = []
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines() #Creará una lista con cada línea separada por commas
        print("")
        print("********** Comunas de Chile **********\n")
        for i in lineas:
            linea = i.split(",")    #Separa líneas por commas
            listaUsuario = linea[2] + " -> " + "[" + linea[3] + "]" #Genera el menú al usuario
            print(listaUsuario)
            nombreComunas.append(linea[2])
            codigoComunas.append(linea[3])
    
    return nombreComunas, codigoComunas

def comunayDatosSeleccionados(comuna): #definimos la funcion
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines()
        for i in lineas:
            linea = i.split(",")
            if comuna in linea:   #Recorre la lista para verificar si existe o no el nombre de la comuna
                for j in range(len(linea)):
                    if linea[j] == comuna:
                        comunaSeleccionada = linea[j:]  #Variable que almacena la lista de la comuna seleccionada y todos sus datos
                        for n, h in enumerate(comunaSeleccionada):  #Bucle que reemplazará elementos vacíos por ceros
                            if h == "":
                                comunaSeleccionada[n] = 0.0
        return comunaSeleccionada

def datosGraficoNoAcumuladosComuna(selectComuna):   #Función para ubicar los últimos 7 datos requeridos de la comuna seleccionada
    reversing = selectComuna[::-1]                  #para los datos no acumulados.
    reversing.pop(0)
    listaFechas = reversing[0:8]
    datosComuna = listaFechas[::-1]
    listaNoAcumulados = []
    for i in range(len(datosComuna)-1): #el for recorrerá la lista cortada para agregar los datos no acumulados a una nueva lista
        listaNoAcumulados.append(int(float(datosComuna[i+1])) - int(float(datosComuna[i]))) #Se restarán los datos y se cambiará el tipo de dato a entero para el gráfico
    return listaNoAcumulados

def datosGraficoAcumuladosComuna(selectComuna): #Función para ubicar los últimos 7 datos requeridos de la comuna seleccionada para los datos acumulados.
    reversing = selectComuna[::-1]  #Invierto la lista de la comuna seleccionada
    reversing.pop(0)    #elimino el primer dato luego de invertir la lista 
    listaFechas = reversing[0:7]    #Selecciono las 7 últimas fechas
    datosComuna = listaFechas[::-1]  #Revierto nuevamente para volver al orden inicial con las 7 fechas seleccionadas
    return datosComuna

def graficoAcumuladosComuna(fechas,datosAcumuladosComuna):  #función para graficar los datos no acumulados de la comuna
    ejex = fechas
    ejey = datosAcumuladosComuna
    plt.title('Contagios Acumulativos Comuna')
    plt.xlabel('Fechas')
    plt.ylabel('Cantidad de contagios')
    plt.plot(ejex,ejey)
    plt.show()

def graficoNoAcumuladosComuna(fechas,datosNoAcumuladosComuna):  #función para graficar los datos acumulados de la comuna
    ejex = fechas
    ejey = datosNoAcumuladosComuna
    plt.title('Contagios No Acumulativos Comuna')
    plt.xlabel('Fechas')
    plt.ylabel('Cantidad de contagios')
    plt.plot(ejex,ejey)
    plt.show()

#------------------------------------------------------------------------------------------------------------------
#-----------------------------------------      REGIONES     ------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

def listadoDeRegiones():    #Función para mostrar al usuario el listado de regiones y sus códigos respectivamente
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
        print("********** Regiones de Chile **********\n")
        for elemento in range(0, 17):   #Mostrará el menú de regiones al usuario sin repetir sus nombres y códigos respectivamente
            listaUsuario2 = regionesNoRepetidas[elemento] + " -> " + "[" + codigosNoRepetidos[elemento] + "]"
            print(listaUsuario2)
        return regionesNoRepetidas, codigosNoRepetidos

def regionyDatosSeleccionadosAcumulados(region):    #Función para crear las últimas 7 fechas 
    listaCompleta = []  #se almacenarán los datos correspondientes a las 7 últimas fechas ordenadamente
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines()
        lineas.pop(0)
        for i in lineas:
            linea = i.split(",")
            if region in linea:
                for j in range(len(linea)):
                    if linea[j] == region:
                        regionSeleccionada = linea[j:]          #Variable asignada para crear una lista desde la región seleccionada
                        reversing = regionSeleccionada[::-1]    #Invierte la lista de las comunas según la región seleccionada
                        reversing.pop(0)                        #Elimino la primera posición (tasa de datos)
                        listaFechas = reversing[0:7]            #Tomo las primeras 7 posiciones (fechas)
                        datosRegiones = listaFechas[::-1]       #Reinvierto la posición de las fechas para el gráfico
                        listaCompleta.append(datosRegiones)     #Agrego los datos a una nueva lista
                        for n, h in enumerate(reversing):  #Bucle que reemplazará elementos vacíos por ceros
                            if h == "":
                                reversing[n] = 0.0
    sumarIndices = []
    for i in range(0, len(listaCompleta[0])):   #Recorro con un for, cada primer elemento de la nueva lista correspondiente a una matriz
        suma = 0    #Inicio variable suma en cero
        for j in range(0, len(listaCompleta)):  #Recorro con otro for, los elementos dentro de la matriz
            suma = suma + float(listaCompleta[j][i])    #Sumo cada primer elemento entre sí
        sumarIndices.append(suma)   #Agrego la suma de dichos elementos a la lista vacía sumarIndices
    
    return sumarIndices

def regionyDatosSeleccionadosNoAcumulados(region): #definimos funcion
    listaCompleta = []
    with open("Datos.csv", "r", encoding="utf-8") as file:
        lineas = file.read().splitlines()   
        lineas.pop(0)   #se elimina la sección primaria del listado para ocupar solamente los datos relevantes para las estadísticas
        for i in lineas:
            linea = i.split(",")
            if region in linea:
                for j in range(len(linea)):
                    if linea[j] == region:
                        regionSeleccionada = linea[j:]          #Variable asignada para crear una lista desde la región seleccionada
                        reversing = regionSeleccionada[::-1]    #Invierte la lista de las comunas según la región seleccionada
                        reversing.pop(0)                        #Elimino la primera posición (tasa de datos)
                        listaFechas = reversing[0:8]            #Tomo las primeras 7 posiciones (fechas)
                        datosRegiones = listaFechas[::-1]       #Reinvierto la posición de las fechas para el gráfico
                        listaCompleta.append(datosRegiones)     #Agrego los datos a una nueva lista
                        for n, h in enumerate(reversing):  #Bucle que reemplazará elementos vacíos por ceros
                            if h == "":
                                reversing[n] = 0.0
    sumarIndices = []
    for i in range(0, len(listaCompleta[0])):   #Recorro con un for, cada primer elemento de la nueva lista correspondiente a una matriz
        suma = 0    #Inicio variable suma en cero
        for j in range(0, len(listaCompleta)):  #Recorro con otro for, los elementos dentro de la matriz
            suma = suma + float(listaCompleta[j][i])    #Sumo cada primer elemento entre sí
        sumarIndices.append(suma)   #Agrego la suma de dichos elementos a la lista vacía sumarIndices
    
    listaNoAcumulados = []
    for j in range(len(sumarIndices)-1): #el for recorrerá la lista cortada para agregar los datos no acumulados a una nueva lista
        listaNoAcumulados.append(int(float(sumarIndices[j+1])) - int(float(sumarIndices[j]))) #Se restarán los datos y se cambiará el tipo de dato a entero para el gráfico
    return listaNoAcumulados

def graficoAcumuladosRegion(fechas,selectRegionAcum):   #función para graficar los datos acumulados de la región seleccionada
    ejex = fechas
    ejey = selectRegionAcum
    plt.title('Contagios Acumulativos Región')
    plt.xlabel('Fechas')
    plt.ylabel('Cantidad de contagios')
    plt.plot(ejex,ejey)
    plt.show()

def graficoNoAcumuladosRegion(fechas,selectRegionNoAcum):   #función para graficar los datos no acumulados de la región seleccionada
    ejex = fechas
    ejey = selectRegionNoAcum
    plt.title('Contagios No Acumulativos Región')
    plt.xlabel('Fechas')
    plt.ylabel('Cantidad de contagios')
    plt.plot(ejex,ejey)
    plt.show()

#------------------------------------------------------------------------------------------------------------------
#-----------------------------------------      MENÚ USUARIO     --------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

print("***** Menú de selección *****")
print("(1) Filtrar comunas.")
print("(2) Filtrar regiones.")
print("(3) Salir.")
filtro = input("Ingrese la opción según el número correspondiente: ")
while int(filtro) < 1 or int(filtro) > 3: # condicion para que el usuario ingrese solamente los numeros correspondientes
    print("Error en la selección. Favor ingrese la opción que se muestra en el menú.")
    filtro = input(">>> ")

fechas = filtrarUltimasFechas() #Llamado a la función para filtrar las últimas 7 fechas

if filtro == "1":   #Selección de comunas
    listadoComunas = listadoDeComunas()
    comuna = input("Ingrese el nombre o código de la comuna: ")
    while comuna not in listadoComunas[0] and comuna not in listadoComunas[1]: #while para hacerle saber al usuario que se a equivocado en escribir su opcion deseada
        print("Nombre o código de la comuna ingresada no es válida.")
        comuna = input("Ingrese nuevamente: ")
    print("Mostrar gráfico de contagios acumulativos para la comuna -> Ingrese (a).")
    print("Mostrar gráfico de contagios no acumulativos para la comuna -> Ingrese (b).")
    opcion = input("Ingrese (a) o (b): ")
    while opcion != "a" and opcion != "b": #while para decirle al usuario que ha ingresado opciones no validas
        print("Error en la selección. Favor ingrese (a) o (b) según la indicación previamente mostrada.")
        opcion = input("Ingrese (a) o (b) nuevamente: ")
    if opcion == "a":    #Mostrará gráfico de contagios acumulativos de la comuna seleccionada
        selectComuna = comunayDatosSeleccionados(comuna)
        datosAcumuladosComuna = datosGraficoAcumuladosComuna(selectComuna)
        graficoAcumuladosComuna = graficoAcumuladosComuna(fechas,datosAcumuladosComuna)
    else:   #Mostrará gráfico de contagios no acumulativos de la comuna seleccionada
        selectComuna = comunayDatosSeleccionados(comuna)
        datosNoAcumuladosComuna = datosGraficoNoAcumuladosComuna(selectComuna)
        graficoDatosNoAcumuladosComuna = graficoNoAcumuladosComuna(fechas, datosNoAcumuladosComuna)
    
elif filtro == "2": #Selección de regiones
    listadoRegiones = listadoDeRegiones()
    region = input("Ingrese el nombre o código de la región: ")
    while region not in listadoRegiones[0] and region not in listadoRegiones[1]: #while para decirle al usuario que se ha equivocado al escribir el codigo o nombre de la region seleccionada
        print("Nombre o código de la Región ingresada no es válida.")
        region = input("Ingrese nuevamente: ")
    print("Mostrar gráfico de contagios acumulativos para la región -> Ingrese (a).")
    print("Mostrar gráfico de contagios no acumulativos para la región -> Ingrese (b).")
    tipoDeGrafico = input("Ingrese (a) o (b): ")
    while tipoDeGrafico != "a" and tipoDeGrafico != "b": #while para decirle al usuario que se ha introducido opciones noo validas
        print("Error en la selección. Favor ingrese (a) o (b) según la indicación previamente mostrada.")
        tipoDeGrafico = input("Ingrese (a) o (b) nuevamente: ")
    if tipoDeGrafico == "a":    #Mostrará gráfico de contagios acumulativos de la región seleccionada
        selectRegionAcum = regionyDatosSeleccionadosAcumulados(region)
        graficoAcumuladosRegion = graficoAcumuladosRegion(fechas,selectRegionAcum)
    else:   #Mostrará gráfico de contagios no acumulativos de la región seleccionada
        selectRegionNoAcum = regionyDatosSeleccionadosNoAcumulados(region)
        graficoNoAcumuladosRegion = graficoNoAcumuladosRegion(fechas, selectRegionNoAcum)

else:   #Selección de Salir
    print("")
    print("\033[1;32;40m\n")
    print("*" * 40)
    print("   ¡Muchas gracias por su preferencia!")
    print("*" * 40)
    print("")