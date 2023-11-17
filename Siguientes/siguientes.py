import re

class reglaProduccion:
    
    def __init__(self, b, p):
        self.base = b
        self.produccion = p

    def getBase(self):
        return self.base

    def getProduccion(self):
        return self.produccion

    def setBase(self, b):
        self.base = b
    
    def setProduccion(self, p):
        self.produccion = p
    
    def __str__(self):
        return self.base + " -> " + self.produccion + ";"
    
    

def obtencionSiguientes(reglasProducccion): #Recibe un arreglo de reglas de producción
    simbolos_inicial = reglasProduccion[0].getBase()
    print("Simbolo inicial: ", simbolos_inicial)
    
    desgloce_elementos_produccion = []
    pass


#script
#Desglozamos la regla que entre
reglaproduccion = "A -> a;"
base = reglaproduccion.split("->")[0].strip() #Se retorna el primer elemento
produccion = reglaproduccion.split("->")[1].strip() #Se retorna lo que produce

#print("Regla de produccion: ", reglaproduccion)
#print("Base: ", base)
#print("produccion: ", produccion)

reglasProduccion = []
rp = reglaProduccion(base, produccion)
reglasProduccion.append(rp)

obtencionSiguientes(reglasProduccion)
