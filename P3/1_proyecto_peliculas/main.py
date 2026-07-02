"""
Crear un proyecto que permita gestionar (administrar) peliculas.
colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas.


Notas:
1.- Utilizar funciones y mandar a llamar desde otros archivos (modulos)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero.idioma) de peliculas
3.- Utilizar o implementar BD relacional con MySQL para gauradar la informacion.
"""
import peliculas
pelis=[]
opc="1"
while opc!="7":
    peliculas.borrarPantalla()
    opc=peliculas.menuPrincipal()
    
    match opc:
        case "1":
            peliculas.borrarPantalla()
            peliculas.agregarPeliculas(pelis)
        case "2":
            peliculas.borrarPantalla()
            peliculas.borrarPeliculas(pelis)
        case "3":
            peliculas.borrarPantalla()
            peliculas.modificarPeliculas(pelis)
        case "4":
            peliculas.borrarPantalla()
            peliculas.mostrarPeliculas(pelis)
        case "5":
            peliculas.borrarPantalla()
            peliculas.buscarPeliculas(pelis)
        case "6":
            peliculas.borrarPantalla()
            peliculas.limpiarPeliculas(pelis)
        case "7":
            peliculas.borrarPantalla()
            peliculas.terminar(pelis)
        case _:
            peliculas.opcionInvalida()