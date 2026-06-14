# """

 
#  Sets.- 
#   Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

#   Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
# """
# set1={"Python", "SQL", "Estructurado", "SQL"}
# print(set1)

# for i in set1:
#   print(i)



# #ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

# #Solucion1
# email=input("Dame tu email:")
# set4={""}
# set4.pop()
# set4.add(email)
# print(f"Emails: {set4}")
# ...
# emails=[]
# opc="S"
# while opc=="S":
#   emails.append(input("Ingresa un email:").lower().strip())
#   opc=input("¿Deseas ingresar otro email (S/N)").upper().strip()
# print(emails)
# ...
# list_emails=[]
# set_emails={""}
# set_emails.clear()
# opc="S"
# while opc=="S":
#   list_emails.append(input("Ingresa un email:").lower().strip())
#   set_emails.add(input("Ingresa un email:").lower().strip())
#   opc=input("¿Deseas ingresar otro email (S/N)").upper().strip()
# print(list_emails)
# print(set_emails)
# ...
# emails=[]
# opc="S"
# while opc=="S":
#   emails.append(input("Ingresa un email:").lower().strip())
#   opc=input("¿Deseas ingresar otro email (S/N)").upper().strip()
# print(emails)
# set_emails=set(list_emails)
# list_emails=list(set_emails)
# print(list_emails)
# ...
# #simulacro
# emails=[]
# continuar=True

# while continuar==True:
    
#     emails.insert(0,input("Ingresa un email: ").lower().strip())
#     opc=input("¿Deseas ingresar otro email (S/N): ").upper().strip()
    
#     if opc=="N":
#         continuar=False

# print("Lista original:")
# print(emails)
# set_emails=set(emails)
# list_emails=list(set_emails)
# print("Lista final sin duplicados:")
# print(list_emails)


#Solucion 2
def areaCirculo(area,r):
  area=area*r*r
  return area

area=[3.1416]
continuar=True

while continuar==True:
  area.insert(0,input("Ingresa el area:"))
  r=input("Introduce el area:")
  areaCirculo()
  opc=input(" ¿Deseas ingres otro email (S/N):").upper().strip()
  if opc=="N":
    continuar=False
    
resultado=areaCirculo(area,r)
print(f"El resultado es: {resultado}")

    


  



