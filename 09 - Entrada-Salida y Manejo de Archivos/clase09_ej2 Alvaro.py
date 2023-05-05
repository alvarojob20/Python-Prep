import sys

if len(sys.argv) == 4:
    
    import datetime
    import os

    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo))

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]

    informacion = str(marca_de_tiempo)+','+temperatura+' ºC'+','+humedad+'%'+','+lluvia

    info = open('clase09_ej2 Alvaro.csv', 'a')
    info.write(informacion+'\n')
    info.close()

else:
    print('ERROR: Verificar informacion ingresada')
    print('Ejemplo: clase09_ej2 Alvaro.py <temperatura en grados centigrados> <humedad> <True/False>')