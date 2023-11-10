# Función para obtener la expresión regular
def cargar_palabras_reservadas(lineas):
    for linea in lineas:
        lista_pReservadas.append(linea.strip('\n'))
        
def cargar_simbolos(lineas):
    for linea in lineas:
        lista_simbolos.append(linea.strip('\n'))

# Leer el archivo de entrada
archivo_cargado = 'palabras_reservadas.txt'
with open(archivo_cargado, 'r') as file:
    lineas = file.readlines()

lista_pReservadas = []
cargar_palabras_reservadas(lineas)

archivo_cargado = 'simbolos.txt'
with open(archivo_cargado, 'r') as file:
    lineas = file.readlines()
    
lista_simbolos = []
cargar_simbolos(lineas)
