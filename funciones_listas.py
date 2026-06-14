"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]



#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+" "+paises[3])
#solo se puede concatenar con (+ y "")




#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)


# #2do forma
for n in range(0,5):
     print(paises[n])



     


paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#ordenar elementos de una lista
paises.sort()
print(paises)




#dar la vuelta a una lista
paises.reverse()
print(paises)




paises=["Mexico","Canada","EUA","Mexico","Brasil"]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

 


#2da forma
paises.insert(1,"Argentina")
print(paises)
paises.insert(8,"Panama")
print(paises)
paises.append(23)
paises.append(3)
print(paises)

#sin importar el numero siempre lo pondra al final de la fila sin importar el valor que introducimos


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)
#2da forma 
paises.remove("EUA")
print(paises)


#Buscar un elemento dentro de la lista
buscar="Brasil " in paises
if buscar==True:
    print("Soy true")
else:
    print("Soy false")    
print(buscar)


#Contar el numeros de veces que aparece un elemento dentro de una lista



#Conocer la posicion o indice en el que se encuentra un elemento de la lista



#Unir el contenido de una lista dentro de otra lista


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente




