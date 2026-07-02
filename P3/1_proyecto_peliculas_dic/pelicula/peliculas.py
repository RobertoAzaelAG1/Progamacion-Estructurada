import funciones

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR CARACTERISTICAS DE PELICULAS :::... \n")
    caracteristica=input("Ingresa el nombre de la caracteristica: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR CARACTERISTICAS DE LA PELICULAS :::... \n")
    if len(pelis)>0:
        for i in pelis:
          print(f"{i}={pelis[i]}")
    else:
        print("... ¡No hay caracteristicas de peliculas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
    
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS CARACTERISTICAS DE LA PELICULAS :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    if opc=="si":
        pelis.clear()
        funciones.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR UNA CARACTERISTICA DE LA PELICULAS :::... \n")
    peli=input("Escribe la caracteristicas de la pelicula a buscar: ").lower().strip()
    noencontre=True
    for i in pelis:
        if i==peli:
            print(f"La caracteristica es: {peli} y su valor es: {pelis[peli]}")
            funciones.esperarTecla()
            noencontre=False
    if noencontre:
        input("\n\t... ¡No existe la caracteristica de la  pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA DE LA PELICULA :::... \n")

    peli=input("Escribe la caracteristica de la pelicula: ").lower().strip()

    if peli in pelis:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Estas seguro que deseas borrar esta caracteristica de la pelicula (Si/No)? ").lower().strip()

        if opc=="si":
            pelis.pop(peli)
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la caracteristica de la pelicula a buscar, verifique! ...")
    
        
        
def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR EL VALOR DE LA CARACTERISTICA DE LA  PELICULAS :::... \n")
    peli=input("Escribe la caracteristica de la pelicula: ").lower().strip()
    noencontre=True
    for i in pelis:
          if peli==i:
                noencontre=False
                print(f"La caracteristica a buscar es: {peli} y su valor es: {pelis[peli]}")
                opc=""
                while opc!="si" and opc!="no":
                  opc=input("¿Estas seguro que deseas modificar el valor de esta caracteristica de la pelicula (SI/NO)? ").lower().strip()
                if opc=="si":
                  pelis[peli]=input("Escribe el nuevo valor de esta caracteristica: ").upper().strip()
                  funciones.accionExitosa()
    if noencontre:
        input("\n\t... ¡No existe la caracteristica de la pelicula a buscar, verifique! ...")