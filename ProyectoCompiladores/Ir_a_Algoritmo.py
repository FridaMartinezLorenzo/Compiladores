
def Ir_a(conjuntoI , simboloAevaluar):
    J = [] #Declaramos la tupla que se va a retornar

    for i, elemento in enumerate(conjuntoI):
        estados = elemento[i+1]
        base = estados[0] #Base de la regla de produccion
        estados = estados[1]
        temporal = [] #Lista temporal para guardar los estados
        bandera_se_detecto_punto = False
        
        for estado in estados: #Obtenemos el listado de estado
            #Vamos a recorrer el punto de la produccion y copiamos en una variable temporal
                if estado == '•':
                    bandera_se_detecto_punto = True
                    print("Se detecto punto")
                    
                if estado != '•' :
                    temporal.append(estado)
                    
                if estado != '•' and bandera_se_detecto_punto == True:
                    temporal.append('•')
                    bandera_se_detecto_punto = False
                    
                print("temporal: ",temporal)
                
        print("temporal saliendo del for: ",temporal)
        J.append([base, temporal]) #Agregamos a la tupla
                    
    return J


conjuntoI =   [         ['I0',   ['S', ['•', 'i', 'p']    ], ['E',['•','i','f']  ]   ]     ]   
print(conjuntoI)
J = Ir_a(conjuntoI,'i')

print (J)