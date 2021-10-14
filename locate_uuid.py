import os
import csv

files = [file for file in os.listdir('./') if '.XML' in file] #Lista de archivos por extención, sí, así me los pasaron en mayúsculas
facturas = [] #Lista de Facturas
uuids = [] # Lista de UUID's

def run():
    for i in files: #Recorrer lista
        with open(i, 'r',encoding='utf-8') as f: #Abrir cada XML
            for line in f:
                if 'Folio' in line: # Buscar esa cadena en la línea
                    lista = line.split() #Cortar por espacios y mandar a una lista
                    for l in lista:
                        if l.startswith('Folio='): #Buscar línea para encontrar el Folio
                            facturas.append(l.replace('Folio','').replace('=','').replace('"','')) #Limpiar 
                if 'UUID' in line: # Buscar esa cadena en la línea
                    lista = line.split() #Cortar por espacios y mandar a una lista
                    for l in lista:
                        if l.startswith('UUID='): #Buscar línea para encontrar el UUID
                            uuids.append(l.replace('UUID','').replace('=','').replace('"','')) #Limpiar
    f.close()
    relacion = {} #Diccionario
    
    for i in range(0,len(facturas)):
        relacion[facturas[i]] = uuids[i] #Llenar el dict recorriendo las dos listas
    

    with open('facturas.csv','w',encoding='utf-8') as f1:   ##
        writer = csv.writer(f1)                             ## Escribir en un .csv para después hacer un BUSCARV en Excel
        for key,value in relacion.items():                  ##
            writer.writerow([key,value])
    f1.close()


if __name__ == '__main__':
    run()