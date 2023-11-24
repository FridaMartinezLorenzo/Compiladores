
def Ir_a(conjuntoI , simboloAevaluar):
    J = [] #Declaramos la tupla que se va a retornar    
    
    for elemento in conjuntoI[1]:
        print("elemento: ",elemento)
        base  = elemento[0] #Base de la regla de produccion
        estados = elemento[1] #Estados de la regla de produccion
        print("estados: ",estados)
        temporal = [] #Lista temporal para guardar los estados
        bandera_se_detecto_punto = bandera_se_encontro_simbolo =False

        for estado in estados: #Obtenemos el listado de estado
            #Vamos a recorrer el punto de la produccion y copiamos en una variable temporal
                if estado == simboloAevaluar:
                    bandera_se_encontro_simbolo = True
                    #print("Se encontro simbolo")
                    
                if estado == '•':
                    bandera_se_detecto_punto = True
                    #print("Se detecto punto")
                    
                if estado != '•':
                    temporal.append(estado)
                    
                if estado != '•' and bandera_se_detecto_punto == True:
                    temporal.append('•')
                    bandera_se_detecto_punto = False
                #print("temporal: ",temporal)
        
        if bandera_se_encontro_simbolo == True:        
            J.append([base, [temporal]]) #Agregamos a la tupla
  
    return J


conjuntoI =           ['I0',  [       ['S', ['•', 'i', 'p'] ], ['E',['•','i','f']  ]      ]   ]     
#print(conjuntoI)
J = Ir_a(conjuntoI,'z')

print(conjuntoI)
print (J)

#K = Ir_a(J,'i')
#print(K)