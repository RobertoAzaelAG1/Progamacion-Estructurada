print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,45,23,33,25,100,-100]
print(numeros)

lista="["
for i in numeros:
    lista+=f"{i},"
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print(f"{lista}]")



    
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["Hola","NBA","Ganador","Perdedor"]
palabra=input("Dame la palabra buscar:")

#1er forma 
if palabra in palabras:
    print(f"La palabra si existe en la lista: {palabra}").upper().strip()
else:
    print(f"Esta palabra: {palabra} , no se encuentra en la lista")



#2DA FORMA
palabras=["Hola","NBA","Ganador","Perdedor"]
palabra=input("Dame la palabra buscar:")

encontre=False
for i in palabras:
    if i==palabra:
        encontre=True

if encontre:
    print(f"La palabra si existe en la lista: {palabra}")
else:
    print(f"Esta palabra: {palabra} , no se encuentra en la lista")       
               
        


    

 

#3er FORMA
palabras=["Hola","NBA","Ganador","Perdedor"]
palabra=input("Dame la palabra buscar:")

encontre=False
for i in palabras:
    if i==palabra:
        encontre=True

if encontre:
    print(f"La palabra si existe en la lista: {palabra}")
else:
    print(f"Esta palabra: {palabra} , no se encuentra en la lista") 
    

palabras=["Hola","NBA","Ganador","Perdedor"]
palabra=input("Dame la palabra buscar:")

encontre=False
i=0
while i<len(palabras):
    if i==palabra:
        encontre=True
    i+=1

if encontre:
    print(f"La palabra si existe en la lista: {palabra}")
else:
    print(f"Esta palabra: {palabra} , no se encuentra en la lista") 

palabras=["Hola","NBA","Ganador","Perdedor"]
palabra=input("Dame la palabra buscar:")

encontre=False
for i in range(0(palabra)):
    if i==palabra:
        encontre=True

if encontre:
    print(f"La palabra si existe en la lista: {palabra}")
else:
    print(f"Esta palabra: {palabra} , no se encuentra en la lista") 



 
    

#Ejemplo 3 Añadir elementos a la lista
lista=[]
true="S"
while true=="S":
    valor=input("Dame un valor de la lista").upper().strip()
    ()
    lista.append(valor)
    true=input=("Deseas añadir otro elemeto a la lista (S/N) ?").upper().strip()
    
   
    


  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["Carlos", "6181234567"],
        ["Juan" , "6182334567"],
        ["Tony", "6182342323"],
       ]
print(agenda)



lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=F"{agenda[r][c]},"
    lista+="\n"
print("["+lista+"]")









for i in agenda:
    print(i)
