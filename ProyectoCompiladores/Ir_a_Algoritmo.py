from cerradura import *

def generar_estado(estado, produccion):
    return [estado, [produccion]]


def Ir_a(I, simboloAevaluar, reglas_prod):
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



#            # Ejemplo de uso
#            conjuntoI = [['E', ['E','•','+', 'T',]], ['E', ['E', '+','•', 'T']], ['T', ['T', '•', 'T', 'F']]]
#            simbolo_evaluar = 'T'
#            reglasProduccion = [('E', ['E', '+', 'T']), ('E', ['T']), ('T', ['T', '*', 'F']), ('T', ['F']), ('F', ['(', 'E', ')']), ('F', ['id'])]
#            J =Ir_a(conjuntoI, simbolo_evaluar, reglasProduccion)
#            
#            print("J: ", J)

#resultado_cerradura = cerradura(conjuntoI, simbolo_evaluar, reglasProduccion)
#print(resultado_cerradura)



#def Ir_a(conjuntoI, simboloAEvaluar, reglas_prod):
#    J=[]
#    print("Estamos trabajando en ir a")
#    estado_actual_I = str(conjuntoI[0])
#    print("estado_actual_I: ", estado_actual_I)
#    
#    for elemento in conjuntoI[1]:
#        if simboloAEvaluar == '$':
    
     
#def Ir_a(conjuntoI, simboloAevaluar, reglas_prod):
#    J = []  # Declaramos la tupla que se va a retornar
#    print("Estamos trabajando en ir a")
#    estado_actual_I = str(conjuntoI[0])
#
#    for elemento in conjuntoI[1]:
#        if simboloAevaluar == '$':
#            J.append("Aceptacion")
#            return J
#
#        print("elemento: ", elemento)
#        base = elemento[0]  # Base de la regla de produccion
#        estados = elemento[1]  # Estados de la regla de produccion
#        print("estados: ", estados)
#        temporal = []  # Lista temporal para guardar los estados
#        bandera_se_detecto_punto = bandera_se_encontro_simbolo = False
#
#        for estado in estados:
#            if estado == simboloAevaluar:
#                bandera_se_encontro_simbolo = True
#
#            if estado == '•':
#                bandera_se_detecto_punto = True
#
#            if estado != '•':
#                temporal.append(estado)
#
#            if estado != '•' and bandera_se_detecto_punto == True:
#                temporal.append('•')
#                bandera_se_detecto_punto = False
#
#        if bandera_se_encontro_simbolo:
#            aux = [base, temporal]
#            J.append(aux)
#    # Imprimimos listas
#    print("\n\nLista de elementos a mandar a cerradura: ", J)
#    
#    for elemento in J:
#        print("elemento: ", elemento)
#    
#    #Hace un caso especial para cuando hay slo un elemento en J
#    if len(J) == 1:
#        print("Hay solo un elemento en J")
#       
#        J.append(estado_actual_I)
#        J.append(J[0])
#        #J = [estado_actual_I, J[0]]
#        print("J: ", J)
#    
#    
#    
#    Lista_aux = []
#    for elemento in J:
#        print("elemento: ", elemento)
#        aux = []
#        aux.append(elemento[0])
#        aux_interno = []
#        for elemento2 in elemento[1]:
#            aux_interno.append(elemento2)
#            print("elemento2: ", elemento2)
#            
#        aux.append([aux_interno])
#        print("aux: ", aux)
#        Lista_aux.append(aux)
#    
#        
#    print("\nLista_aux: ", Lista_aux)
#    
#    J = [estado_actual_I, Lista_aux]
#    
#    print("\nJ: ", J)
#    J = cerradura(J, reglas_prod)
#    return J
#
#

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