import csv


ficherodetallado = '2023_MeteoCat_Detall_Estacions.csv'
ficherosimple = '2020_MeteoCat_Estacions.csv'

def tempmin(fichero):
    temp = 500.00
    with open(fichero) as estacioncsv:
        reader = csv.DictReader(estacioncsv)

        for item in reader:
            if item['ACRONIM'] == 'TN':
                tm = float(item['VALOR'])
                if tm < temp:
                    temp = tm
                    fecha = item['DATA_LECTURA']
                    code = item['CODI_ESTACIO']
    nom=convertidor(ficherosimple,code)
    print("Temperatura minima:",temp,"\nFecha:",fecha,"\nNombre estacion: ",nom)

def convertidor(fichero, code):
    with open(fichero) as estacioncsv:
        reader = csv.DictReader(estacioncsv)

        for item in reader:
            if code == item['CODI_ESTACIO']:
                nom = item['EMPLACAMENT']
    return nom

tempmin(ficherodetallado)
#print(convertidor(ficherosimple,code))