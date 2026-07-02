def borrarPantalla():
    print("\033c")
    
def esperarTecla():
    input("... ¡Oprima cualquier tecla para continuar!")
    
    
    
def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito!...")
    
def menuPrincipal():
    print("\n\t\t...::: M E N U  P R I N C I P A L:::...\n")
    opciones=input("\n\t 1.- Agregar\n\t 2.- Borrar\n\t 3.- Modificar\n\t 4.- Mostrar\n\t 5.- Buscar\n\t 6.- Limpiar\n\t 7.- Salir\n\t\t Elige una Opcion: ").strip()
    return opciones
  
  
def agregarPeliculas(pelis):
    print("\n\t\t...::: AGREGAR PELICULAS:::...\n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis.append(peli)
    accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t...::: MOSTRAR PELICULAS :::...\n")
    if len(pelis)>0:
        print("\n\n\tCodigo\t\tPelicula\n")
    for i in range(0,len(pelis)):
        print(f"{i+1}\t\t{pelis[i]}")
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ...")
    
    
      
def limpiarPeliculas(pelis):
    print("\n\t\t...::: BORRAR TODAS LAS PELICULAS :::...\n")
    opc=input("¿Estas seguro que deseas borrar TODAS LAS PEÑICULAS (Si/No)?").lower().strip()
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS LAS PEÑICULAS (Si/No)?").lower().strip()
    if opc=="si":
        pelis=pelis.clear()
        
def buscarPelicula(pelis):
    print("\n\t\t...::: BUSCAR PELICULAS :::...\n")
    peli=input("Escribe la pelicula a buscar: ").upper().strip()
    if peli in pelis:
        print("\n\n\tCodigo\t\tPelicula\n")
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
                print(f"{i+1}\t\t{pelis[i]}")
        esperarTecla()
    else:
        input("\n\t... ¡No existe la eplicula a buscar, verifique! ...")
        
    
def borrarPelicula(pelis):
    print("\n\t\t...::: BORRAR PELICULAS :::...\n")
    peli=input("Escribe la pelicula: ").upper().strip()
    if peli in pelis:
        opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)?").lower().strip()
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)?").lower().strip()
    if opc=="si":
        pelis.remove(peli)
        accionExitosa()
    else:
        input("\n\t... ¡No existe la eplicula a borrar, verifique! ...")
  
  
def modificarPelicula(pelis):
    print("\n\t\t...::: MODIFICAR PELICULAS :::...\n")
    peli=input("Escribe la pelicula: ").upper().strip()
    if peli in pelis:
        for i in range(0, len(pelis)):
            if peli==pelis[i]:
                 opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)?").lower().strip()
                 while opc!="si" and opc!="no":
                  opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)?").lower().strip()
                 if opc=="si":
                    pelis[i]=input("Escribe el nuevo nombre de la pelicula: ").upper().strip()
                    accionExitosa()
    else:
        input("\n\t... ¡No existe la eplicula a modificar, verifique! ...")  