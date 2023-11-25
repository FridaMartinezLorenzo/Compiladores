from cerradura import *

def generar_estado(estado, produccion):
    return [estado, [produccion]]


def Ir_a(I, simboloAevaluar, reglas_prod):
    if len(I) == 0:
        return None
    
    print("Estamos trabajando en ir a")
    J = []  # Conjunto de elementos vacío
    for elemento in I[1]:
        print("elemento: ", elemento)
        
        produccion = elemento[1]  # Obtener la producción de la regla
        print("produccion: ", produccion)
        for i in range(len(produccion)-1): 
            print("produccion[i]: ", produccion[i])
            if produccion[i] == '•' and produccion[i + 1] == simboloAevaluar:
                # Intercambiar posición con el inmediato siguiente
                nueva_produccion = produccion.copy()
                nueva_produccion[i], nueva_produccion[i + 1] = nueva_produccion[i + 1], nueva_produccion[i]
                J.append(nueva_produccion)
    if len(J) == 0:
        return None
    retornoCerradura = cerradura(['I0',J],reglas_prod)
    print("retornoCerradura: ", retornoCerradura)
    return retornoCerradura  # Supongo 'I0' como ejemplo, ajusta según tu lógica



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