import random
import csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”MiguelSánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = []
dictSueldo = {}
def asignarSueldos(trabajadores):
    sueldos.clear()
    for i in trabajadores:
        sueldo = random.randint(300000,2500000)
        dictSueldo[sueldo] = 1
        trabajador =[i,sueldo]
        sueldos.append(trabajador)
def clasificarSueldos(sueldos):
    sueldoBajo=[]
    sueldoMedio=[]
    sueldoAlto=[]
    for a in sueldos:
        if a[1] < 800000:
            sueldoBajo.append(a)
        elif 800000 <= a [1] <= 2000000:
            sueldoMedio.append(a)
        elif a[1] > 2000000:
            sueldoAlto.append(a)
    print(sueldoBajo)               
def verEstadisticas():
    minimo = min(dictSueldo.keys())
    print(dictSueldo[minimo],minimo)
    maximo =max(dictSueldo.keys())
    print(dictSueldo[minimo],maximo)
    promedio = sum(dictSueldo.keys())/len(dictSueldo.keys())
    print (promedio)            

while True:
    print("""¿Que opcion desea escojer?
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa

          """)
    opcion = int(input(""))
    if opcion == 1:
        asignarSueldos(trabajadores)
        for sueldo in sueldos:
          print(sueldo)
    if opcion == 2:
        clasificarSueldos(sueldos)
    if opcion ==3:
        verEstadisticas()
    if opcion == 5:
        print("Finalizando programa…")   
        print("Desarrollado por Felipe Angel")     
        print("Rut 19.030.780-8")
        break