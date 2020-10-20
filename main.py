# Proyecto Integrador: Inventarios
# Primer Semestre: Pensamiento Computacional para la Ingeniería 
#
# Integrantes: 
# Nombre: Miguel Angel Pedraza Aguilar 
# Matricula: A01284469
#
# Nombre: Adrián Garza Zapata
# Matricula: A01284161
#
# Funciones 

# Funcion inicial para pedir los archivo de inventario a utilizar
def pedirArchivoInventario():
    # Pedimos el archivo
    filename = input("Escriba el nombre de su archivo de inventario: ")
    # Abrimos el archivo
    file = open(filename, "r")
    # Listas donde guardaremos al información
    modelos = []
    descripcion = []
    cantExistentes = []
    # Ciclo para leer por linea
    for line in file:
        # Guardamos la linea en una variable
        listaRenglon = line.split()
        # Agregamos especificamente que parte añadir a la lista en int o string
        modelos.append(int(listaRenglon[0]))
        descripcion.append(listaRenglon[1].lower())
        cantExistentes.append(int(listaRenglon[2]))
    
    # Cerramos el archivo
    file.close()

    # Regresamos las listas
    return modelos, descripcion, cantExistentes

# Funcion inicial para pedir los archivos de ventas a utilizar
def pedirArchivoVentas():
    # Pedimos el archivo
    filename = input("Escriba el nombre de su archivo de ventas y vendedores: ")
    # Abrimos el archivo
    file = open(filename, "r")
    # Listas donde guardaremos al información
    ventas = []
    vendedores = []
    # Ciclo para leer por linea
    for line in file:
        # Guardamos la linea en una variable
        listaRenglon = line.split()
        # Lista de vendedores
        vendedores.append(listaRenglon[0].lower())
        # Matriz de ventas
        renglon = []
        for j in range(1, len(listaRenglon)):
            renglon.append(int(listaRenglon[j]))
        ventas.append(renglon)
    
    # Cerramos el archivo
    file.close()

    # Regresamos las listas
    return ventas, vendedores

# 1. Funcion para registrar las ventas
def registrarVentas(modelos, cantExistentes, ventas, vendedores):
    agregarVenta = True
    while agregarVenta == True:
        # Pedimos el nombre del vendedor
        nombreVendedor = input(("Escriba el nombre del vendedor: "))
        print()
        # Ciclo para ver que el vendedor exista
        while nombreVendedor.lower() not in vendedores:
            print("El vendedor que ha escrito no existe. Intente de nuevo")
            nombreVendedor = input(("Escriba el nombre del vendedor: "))
            print()

        # Pedimos la clave del modelo vendido
        modeloVendido = input("Escriba la clave del modelo vendido: ")
        print()
        # Ciclo para asegurarnos de que la clave exista sino pedimos de nuevo
        while True:
            # Condiciones para ver si es numero o si no se encuentra en los modelos existentes
            if modeloVendido.isdigit() == False:
                print("La clave que escribió no es de ningún modelo existente o no es un numero valido. Intente de nuevo.")
                modeloVendido = input("Escriba la clave del modelo vendido: ")
                print()    
            elif int(modeloVendido) not in modelos:
                print("La clave que escribió no es de ningún modelo existente o no es un numero valido. Intente de nuevo.")
                modeloVendido = input("Escriba la clave del modelo vendido: ")
                print()
            else:
                break
        
        # Convertimos el modelo a numero para el resto de operaciones 
        modeloVendido = int(modeloVendido)

        # Pedimos la cantidad vendida
        cantidadVendida = input("Escriba la cantidad de unidades vendidas: ")
        print()

        # Ciclo para ver que la cantidad de numeros vendida sea numero
        while cantidadVendida.isdigit() == False:
            print("¡Error! Recuerde escribir un numero. Intentelo de nuevo")
            cantidadVendida = input("Escriba la cantidad de unidades vendidas: ")
            print()

        # Convertimos el numero de vendidos a numero para el resto de operaciones 
        cantidadVendida = int(cantidadVendida)

        # Variable con el index del modelo vendido
        indexModelo = modelos.index(modeloVendido)
        # Variable con el index del vendeor
        indexVendedor = vendedores.index(nombreVendedor.lower())

        # Condiciones para ver si hay suficientes unidades, si no decir que no hay suficientes unidades
        if cantidadVendida <= cantExistentes[indexModelo]:
            cantExistentes[indexModelo] -= cantidadVendida
            ventas[indexVendedor][indexModelo] += cantidadVendida
            print("¡Se ha registrado la venta con éxito!")
        else:
            print("Lo sentimos, no hay suficentes unidades.")

        # Preguntamos al usuario si quiere regresar al menu
        print()
        volver = input('Si desea registrar otra venta escriba "si". Si desea volver al menu escriba "volver": ')
        print()
       # Ciclo para ver que escriba una de las opciones dadas  
        while volver.lower() != "si" and volver.lower() != "volver":
            print("¡Error! Intente de nuevo.")
            volver = input('Si desea registrar otra venta escriba "si". Si desea volver al menu escriba "volver": ')
            print()
        
        # Condicion para volver o seguir registrando 
        if volver == "volver":
            agregarVenta = False
        else:
            agregarVenta = True

# 2. Funcion para registrar llegadas al almacen
def registrarArtriculosAlmacen(modelos, cantExistentes):
    agregarArticulo = True
    while agregarArticulo == True:
        # Pedimos la clave del articulo traido
        modeloArticulo = input("Escriba la clave del modelo traído: ")
        print()
        # Ciclo para asegurarnos de que la clave exista y sea un numero
        while True:
            if modeloArticulo.isdigit() == False:
                print("Recuerde que debe ingresar un número. Intente de nuevo.")
                modeloArticulo = input("Escriba la clave del modelo traído: ")
                print()
            elif int(modeloArticulo) not in modelos:
                print("La clave que escribió no es de ningún modelo existente. Intente de nuevo.")
                modeloArticulo = input("Escriba la clave del modelo traído: ")
                print()
            else:
                break

        # Lo dejamos como numero para el resto de operaciones
        modeloArticulo = int(modeloArticulo)

        unidadesTraidas = input("Escriba cuantas unidades trajeron: ")
        print()
        while True:
            if unidadesTraidas.isdigit() == False:
                print("Recuerde que debe ingresar un número. Intente de nuevo.")
                unidadesTraidas = input("Escriba cuantas unidades trajeron: ")
                print()
            elif int(unidadesTraidas) < 1:
                print("Ha escriba un numero de unidades invalida.")
                unidadesTraidas = input("Escriba cuantas unidades trajeron: ")
                print()
            else:
                break

        # Dejamos en numero para el resto de operaciones
        unidadesTraidas = int(unidadesTraidas)

        indexModelo = modelos.index(modeloArticulo)
        cantExistentes[indexModelo] += unidadesTraidas
        print("¡Se han registrado las unidades con éxito!")

        # Preguntamos al usuario si quiere regresar al menu
        print()
        volver = input('Si desea registrar otro articulo escriba "si". Si desea volver al menu escriba "volver": ')
        print()
       # Ciclo para ver que escriba una de las opciones dadas  
        while volver.lower() != "si" and volver.lower() != "volver":
            print("¡Error! Intente de nuevo.")
            volver = input('Si desea registrar otro articulo escriba "si". Si desea volver al menu escriba "volver": ')
            print()

        # Condicion para volver o seguir registrando 
        if volver == "volver":
            agregarArticulo = False
        else:
            agregarArticulo = True

# 3. Funcion para consultar el inventario
def consultarInventario(modelos, descripcion, cantExistentes):
    # Ciclo for para imprimir el inventario con sus modelos, descriciones y cantidades
    print("Inventario: Clave, Descripción, Cantidad de unidades disponibles")
    for i in range(len(modelos)):
        print(modelos[i], end=" ")
        print(descripcion[i].capitalize(), end=" ")
        print(cantExistentes[i], end=" ")
        print()
    
    # Preguntamos al usuario si quiere regresar al menu
    print()
    volver = input('Para volver al menu escriba "volver": ')
    if volver == "volver":
        return
    else:
        # Con este ciclo nos aseguramos de que escriba la palabra solicitada
        while volver != "volver":
            volver = input('Para volver al menu escriba "volver": ')

# 4. Funcion para ver el modelo más vendido
def modeloMasVendido(ventas, modelos, descripcion):
    # Declaramos una lista vacia donde pondremos la suma de las columanas de ventas
    sumasDeColumnas = []
    # Hacemos el primer ciclo para leer las columnas
    for i in range(len(ventas[0])):
        # Inicializamos en cero para que una vez que sume y cambie de renglon vuelva a empezar en cero
        suma = 0
        # Segundo ciclo para movernos entre los renglones 
        for j in range(len(ventas)):
            # Sumammos los valores de columna
            suma += ventas[j][i]
        # Los metemos en nuestra lista 
        sumasDeColumnas.append(suma)

    # Usando max sacamos el numero mayor
    masVendido = sumasDeColumnas[0]
    for k in range(len(sumasDeColumnas)):
        if sumasDeColumnas[k] > masVendido:
            masVendido = sumasDeColumnas[k]

    # Despues obtenemos el index de ese numero en la lista de la suma 
    indexMasVendido = sumasDeColumnas.index(masVendido)

    # Imprimimos el modelo y descripcion con el index del numero mayor
    print("El carro más vendido es: ")
    print(modelos[indexMasVendido], end=" ")
    print(descripcion[indexMasVendido].capitalize())

    # Preguntamos al usuario si quiere regresar al menu
    print()
    volver = input('Para volver al menu escriba "volver": ')
    if volver == "volver":
        return
    else:
        # Con este ciclo nos aseguramos de que escriba la palabra solicitada
        while volver != "volver":
            volver = input('Para volver al menu escriba "volver": ')

# 5. Funcion para ver vendedor que ha vendido una mauor cantidad de articulos
def vendedorConMasVentas(ventas, vendedores):
    # Lista para la suma de renglones que equivale a las ventas de los vendedores
    sumaDeRenglones = []
    # Ciclo para recorrer matriz 
    for i in range(len(ventas)):
        suma = 0
        for j in range(len(ventas[0])):
            suma += ventas[i][j]
        sumaDeRenglones.append(suma)
    
    # Sacamos el maximo de ventas
    masVentas = sumaDeRenglones[0]
    for k in range(len(sumaDeRenglones)):
        if sumaDeRenglones[k] > masVentas:
            masVentas = sumaDeRenglones[k]
    masVentasIndex = sumaDeRenglones.index(masVentas)

    # Imprimimos el vendedor con mas ventas
    print(vendedores[masVentasIndex].capitalize() + " es quien ha vendido más unidades. ¡Buen trabajo!")

    # Preguntamos al usuario si quiere regresar al menu
    print()
    volver = input('Para volver al menu escriba "volver": ')
    if volver == "volver":
        return
    else:
        # Con este ciclo nos aseguramos de que escriba la palabra solicitada
        while volver != "volver":
            volver = input('Para volver al menu escriba "volver": ')

# 6. Funcion para ver las ventas de un vendedor
def reporteVentasVenededor(ventas, vendedores, modelos, descripcion):
    agregarReporte = True
    while agregarReporte == True:
        # Pedimos el nombre del vendedor para hacer el reporte
        nombreDelVendedor = input("Escriba el nombre del vendedor que desea ver su reporte: ")
        print()
        # Ciclo para ver si el vendedor existe
        while nombreDelVendedor.lower() not in vendedores:
            print("Ese vendedor no existe. Intente de nuevo.")
            nombreDelVendedor = input("Escriba el nombre del vendedor que desea ver su reporte: ")
            print()
        
        # Abrimos un archivo
        nombreArchivo = input("¿Como quiere llamar el archivo? ")
        file = open(nombreArchivo, "w")
        indexNombre = vendedores.index(nombreDelVendedor.lower())
        file.write("REPORTE DE VENTAS DE " + vendedores[indexNombre].upper() + "\n")
        file.write("Nombre: " + vendedores[indexNombre].capitalize() + "\n")
        # Ciclo para revisar y escribir en el archivo las claves nombres y ventas que este vendedor ha tenido
        for i in range(len(modelos)):
            file.write("Clave: " + str(modelos[i]) + " Descripción: " + descripcion[i].capitalize() + " Vendidos: " + str(ventas[indexNombre][i]) + "\n")
        # Cerramos el archivo
        file.close()

        # Imprimimos que se realizo el reporte con exito  
        print()
        print("¡Reporte generado con éxito! El archivo se llama " + nombreArchivo + ".")

        # Preguntamos al usuario si quiere regresar al menu
        print()
        volver = input('Si desea generar otro reporte escriba "si". Si desea volver al menu escriba "volver": ')
        print()
       # Ciclo para ver que escriba una de las opciones dadas  
        while volver.lower() != "si" and volver.lower() != "volver":
            print("¡Error! Intentelo de nuevo.")
            volver = input('Si desea generar otro reporte escriba "si". Si desea volver al menu escriba "volver": ')
            print()
        
        # Condicion para volver o seguir registrando 
        if volver == "volver":
            agregarReporte = False
        else:
            agregarReporte = True

# 7. Funcion para NUESRTRA PROPUESTA
def propuesta(modelos, descripcion, cantExistentes, ventas):
    agregarCarro = True
    while agregarCarro == True:
        # Pedimos que se le asigne una clave
        nuevaClave = input("Eliga una clave para el nuevo vehículo: ")
        print()
        # Ciclo para revisar que sea numero y si esa clave ya existe
        while True:
            if nuevaClave.isdigit() == False:
                print("Error, intente de nuevo. Recuerde que debe escribir un numero entero")
                nuevaClave = input("Eliga una clave para el nuevo vehículo: ")
                print()
            elif int(nuevaClave) in modelos:
                print("Error, intente de nuevo. La clave escrita ya existe.")
                nuevaClave = input("Eliga una clave para el nuevo vehículo: ")
                print()
            else:
                break
        
        # Dejamos la clave como numero
        nuevaClave = int(nuevaClave)

        # Pedimos el nombre del carro
        nuevaDescripcion = input("Escriba el nombre del vehículo: ")
        print()
        while nuevaDescripcion.lower() in descripcion:
            print("Error, ese nombre de articulo ya existe. Intentelo de nuevo.")
            nuevaDescripcion = input("Escriba el nombre del vehículo: ")
            print()

        # Pedimos la cantidad 
        cantidad = input("Cuantas unidades trajeron: ")
        print()
        # Validamos que sea numero con ciclo para ver si es numero o no
        while True:
            if cantidad.isdigit()==False:
                print("Error, intente de nuevo. Recuerde que debe escribir un numero entero")
                cantidad = input("Eliga una clave para el nuevo vehículo: ")
                print()
            elif int(cantidad) < 1:
                print("Error, intente de nuevo. La cantidad escrita no es valida.")
                cantidad = input("Eliga una clave para el nuevo vehículo: ")    
                print()
            else:
                break

        # Lo dejamos con valor de numero para el resto de operaciones
        cantidad = int(cantidad)

        # Agregamos todo a sus respectivas listas
        modelos.append(nuevaClave)
        descripcion.append(nuevaDescripcion)
        cantExistentes.append(cantidad)

        # Ciclo para agregar otro espacio en la lista de ventas
        for v in ventas:
            v.append(0)

        # Imprimimos que que se registro
        print("¡Se ha registrado el nuevo vehículo con éxito!")

        # Preguntamos al usuario si quiere regresar al menu
        print()
        volver = input('Si desea agregar otro vehículo escriba "si". Si desea volver al menu escriba "volver": ')
        print()
       # Ciclo para ver que escriba una de las opciones dadas  
        while volver.lower() != "si" and volver.lower() != "volver":
            print("¡Error! Intentelo de nuevo.")
            volver = input('Si desea agregar otro vehículo escriba "si". Si desea volver al menu escriba "volver": ')
            print()
        
        # Condicion para volver o seguir registrando 
        if volver == "volver":
            agregarCarro = False
        else:
            agregarCarro = True

# Function intro donde esta el menu y llamamos y relizamos el resto de funciones
def intro(modelos, descripcion, cantExistentes, ventas, vendedores): 
    print("******************************************************************************************************************")
    print("*                                          BIENVENIDO AL INVENTARIO                                              *")
    print("******************************************************************************************************************")
    print()
    print("MENU: Escriba el numero de la actividad que desea realizar")
    print("1. Registrar ventas")
    print("2. Registrar llegada de artículos al almacén")
    print("3. Consultar datos del inventario disponible")
    print("4. Consultar cuál es el modelo del artículo más vendido")
    print("5. Consultar cuál vendedor ha vendido una cantidad mayor de artículos")
    print("6. Reporte de ventas de un vendedor")
    print("7. Agregar nuevo vehiculo al almacen")
    print("8. Salir")
    print()

    # Pedimos la actividad a realizar
    actividad = input('Eliga un numero de actividad a realizar (1-7) o escriba 8 para terminar: ')

    # Ciclo para validar que sea numero entre 1 y  
    while actividad not in "12345678":
        actividad = input('Error, pruebe de nuevo. Eliga un numero de actividad (1-7) o escriba 8 para terminar: ')
        

    # Condiciones para ver que actividad eligio
    if actividad == "1":
        print()
        print("Ha elegido: Registrar Ventas")
        print()
        registrarVentas(modelos, cantExistentes, ventas, vendedores)
    elif actividad == "2":
        print()
        print("Ha elegido: Registrar llegada de artículos al almacén") 
        print()
        registrarArtriculosAlmacen(modelos, cantExistentes)
    elif actividad == "3":
        print()
        print("Ha elegido: Consultar datos del inventario disponible")
        print()
        consultarInventario(modelos, descripcion, cantExistentes)
    elif actividad == "4":
        print()
        print("Ha elegido: Consultar cuál es el modelo del artículo más vendido")
        print()
        modeloMasVendido(ventas, modelos, descripcion)
    elif actividad == "5":
        print()
        print("Ha elegido: Consultar cuál vendedor ha vendido una cantidad mayor de artículos")
        print()
        vendedorConMasVentas(ventas, vendedores)
    elif actividad == "6":
        print()
        print("Ha elegido: Reporte de ventas de un vendedor")
        print()
        reporteVentasVenededor(ventas, vendedores, modelos, descripcion)
    elif actividad == "7":
        print()
        print("Ha elegido: Agregar nuevo vehiculo al almacen")
        print()
        propuesta(modelos, descripcion, cantExistentes, ventas)
    else:
        print()
        print("Cerrando sesión. ¡Vuelva pronto!")
        print()
        quit()

# Funcion main 
def main():
    print()
    modelos, descripcion, cantExistentes = pedirArchivoInventario()
    ventas, vendedores = pedirArchivoVentas()
    print()
    while True:
        intro(modelos, descripcion, cantExistentes, ventas, vendedores)

# Inicia el programa 
main()