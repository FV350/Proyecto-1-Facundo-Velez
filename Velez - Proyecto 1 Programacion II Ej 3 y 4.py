#Ejercicio 1: Expresiones regulares

#Matrículas válidas:

#LV-QWE
#LQ-ABE
#LV-X443
#LV-S586
#LV-SX334

#Matrículas inválidas:

#LA-123
#LX-ABC
#LV
#LV-344

#Respuesta: ^L\w\W?\w?\w?\w?\w?\w?

#Ejercicio 2: Expresiones regulares

#1901
#1900
#1850
#500
#12
#2

#Respuesta: ^((1900)|(1[0-8][0-9]{2})|([1-9][0-9]{2})|([1-9][0-9]{1})|([1-9]))$

#Ejercicio 3: Recursión
#punto 1: MAL

def RecursionUnoyDos(numero):
    i = 0
    recurlist = []
    listnum = [int(a) for a in str(numero)]
    if listnum[i] % 2 == 0:
        recurlist.append(1)
        i = i + 1
        print(recurlist)
    elif listnum[i] % 2 != 0:
        recurlist.append(2)
        i = i + 1
        RecursionUnoyDos(numero)


print(RecursionUnoyDos(153454))

#Punto 2:



