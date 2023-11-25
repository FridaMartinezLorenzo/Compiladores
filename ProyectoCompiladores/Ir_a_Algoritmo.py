from cerradura import *

from cerradura import *

def generar_estado(estado, produccion):
    return [estado, [produccion]]

def Ir_a(conjuntoI, simboloAevaluar, reglas_prod):
    J = []  # Declaramos la tupla que se va a retornar
    print("Estamos trabajando en ir a")
    estado_actual_I = str(conjuntoI[0])

    for elemento in conjuntoI[1]:
        if simboloAevaluar == '$':
            J.append("Aceptacion")
            return J

        print("elemento: ", elemento)
        base = elemento[0]  # Base de la regla de produccion
        estados = elemento[1]  # Estados de la regla de produccion
        print("estados: ", estados)
        temporal = []  # Lista temporal para guardar los estados
        bandera_se_detecto_punto = bandera_se_encontro_simbolo = False

        for estado in estados:
            if estado == simboloAevaluar:
                bandera_se_encontro_simbolo = True

            if estado == '•':
                bandera_se_detecto_punto = True

            if estado != '•':
                temporal.append(estado)

            if estado != '•' and bandera_se_detecto_punto == True:
                temporal.append('•')
                bandera_se_detecto_punto = False

        if bandera_se_encontro_simbolo:
            aux = [base, temporal]
            J.append(aux)
    # Imprimimos listas
    print("\n\nLista de elementos a mandar a cerradura: ", J)
    
    for elemento in J:
        print("elemento: ", elemento)
    
    
    Lista_aux = []
    for elemento in J:
        print("elemento: ", elemento)
        aux = []
        aux.append(elemento[0])
        aux_interno = []
        for elemento2 in elemento[1]:
            aux_interno.append(elemento2)
            print("elemento2: ", elemento2)
            
        aux.append(aux_interno)
        print("aux: ", aux)
        Lista_aux.append(aux)
    
        
    print("\nLista_aux: ", Lista_aux)
    
    J = [estado_actual_I, Lista_aux]
    
    print("\nJ: ", J)
    J = cerradura(J, reglas_prod)
    return J



# Resto del código...



'''

conjuntoI =           ['I0',  [       ['S', ['•', 'i', 'p'] ], ['E',['•','i','f']  ]      ]   ]   , ['I1',  [       ['S', ['•', 'i', 'p'] ], ['E',['•','i','f']  ]      ]   ]     
for e in conjuntoI:
    print(e)
    
#conjuntoI = conjuntoI[1:]

conjuntoI = list(conjuntoI)
del conjuntoI[0]
print(conjuntoI)
# J = Ir_a(conjuntoI,'i')

#print(conjuntoI)
#print (J)

'''