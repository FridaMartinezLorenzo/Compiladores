from cerradura import *

def generar_estado(estado, produccion):
    return [estado, [produccion]]


def Ir_a(I, simboloAevaluar, reglas_prod, nuevo_elemento_canonica):
    if len(I) == 0:                                 # Si el conjunto I está vacío
        return None
        
    if simboloAevaluar == '$':                     # Si el símbolo a evaluar es el símbolo de fin de cadena
        return "Aceptacion"
    
    #print("Estamos trabajando en ir a")
    J = []  # Conjunto de elementos vacío
    for elemento in I[1]:
        #print("elemento: ", elemento)
        base = elemento[0]                          # Obtener el símbolo base de la regla
        produccion = elemento[1]                    # Obtener la producción de la regla
        #print("produccion: ", produccion)
        
        for i in range(len(produccion)-1): 
            print("produccion[i]: ", produccion[i])
            print("produccion", produccion)
            print("len(produccion)", len(produccion))
            if produccion[i] == '•' and len(produccion) == 1:
               print("Se detecta la produccion lambda")
               nuevo_elemento_canonica.setEnviadoACerradura(produccion)  
               retornoCerradura = cerradura(['I0',produccion],reglas_prod)  
               #print("retornoCerradura: ", retornoCerradura)
               return retornoCerradura  
            
            if produccion[i] == '•' and produccion[i + 1] == simboloAevaluar:  # Intercambiar posición con el inmediato siguiente
                nueva_produccion = produccion.copy()
                nueva_produccion[i], nueva_produccion[i + 1] = nueva_produccion[i + 1], nueva_produccion[i]
                print(nueva_produccion)
                new =[base,nueva_produccion]
                J.append(new)
    
    if len(J) == 0:                                      #El conjunto J está vacío
        return None
    print("J agregando:", J)
    nuevo_elemento_canonica.setEnviadoACerradura(J)      # Agregamos el conjunto J a la tabla de datos para la coleccion canonica, para identificar que se envio a la cerradura
    #print(nuevo_elemento_canonica)
    retornoCerradura = cerradura(['I0',J],reglas_prod)   # Se obtiene el conjunto de elementos resultante de la cerradura
    print("retornoCerradura: ", retornoCerradura)
    return retornoCerradura                              # Devolver el conjunto de elementos

