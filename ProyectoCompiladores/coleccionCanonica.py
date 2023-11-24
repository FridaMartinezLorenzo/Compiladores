
#Funcion reciclada de primeros
def calcularReglasP(archivo,listaNoTerminales):
    listaProducciones=[]#contiene las tuplas de las producciones
    cadena = []
    lineas = archivo.readlines()   
    #print(len(lineas))
    archivo2=open(str(ruta),encoding="utf-8")
    archivo2.readline()#Salto de linea en el archivo
    archivo2.readline()
    #print(len(lineas))
    for l in lineas:#Obtener las producciones de cada no terminal
        cadena=[]
        reglaP = archivo2.readline().split("->")  # separa el no terminal de la produccion
        reglaP[1] = reglaP[1].replace("\n", "")  # quita el salto de linea
        indice = 0
        cad=reglaP[1]
        while indice < len(cad):
            aux=""
            if cad[indice] == ' ':
                indice+=1
            if indice < len(cad):
                caracter = cad[indice]  
                if caracter.isupper() == True:
                    cadena.append(caracter)
                    indice += 1
                elif caracter.isalpha() == False:
                    cadena.append(caracter)
                    indice += 1
                else:
                    while caracter.islower() == True and indice < len(cad):
                        caracter = cad[indice]
                        aux+=caracter
                        indice += 1
                    cadena.append(aux)
        producciones = (reglaP[0], cadena)
        listaProducciones.append(producciones)

    return listaProducciones




##############################################################################################################
#Abre archivo gramatica.txt

ruta="gramatica.txt"
archivoGramatica=open(ruta,encoding="utf-8")#Usar esta codificacion para que lea lambda
##Variables
noTerminales=archivoGramatica.readline().split()
terminales=archivoGramatica.readline().split()
simboloInicial = noTerminales[0]
noTerminales=[]
terminales=[]
primerosArray=[]
reglasProduccion=[]
reglasProduccion=calcularReglasP(archivoGramatica,noTerminales)
print(reglasProduccion)


elemento_gramatica_aumentada = [simboloInicial + "'", [simboloInicial,"$"]]
#Aumentar gramatica
reglasProduccion.insert(0,elemento_gramatica_aumentada)

print(reglasProduccion)
