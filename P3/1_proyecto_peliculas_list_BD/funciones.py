import mysql.connector

def borrarPantalla():
    print("\033c")
    
def esperarTecla():
    input("... ¡Oprima cualquier tecla para continuar! ...")
    
def terminar():
    input(".... :::: !GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! ::::.... ")
    
def opcionInvalida():
    input("\n\t .... ¡Opcion invalidad oprima cualquier tecla para continuar !....")

def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito!...")
    
def accionNoExitosa():
    input("\n\t...¡Accion NO Realizada con Exito!...")
    
def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas_v1"
        )
        return conexion
        
    except:
        borrarPantalla()
        input("...¡Por el momento NO es posible conectarse con el sistema o aplicacion y la base de datos porfavor intentelo mas tarde!...")
        return None