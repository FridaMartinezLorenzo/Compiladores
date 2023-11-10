import re

# Función para generar el alfabeto a partir de las líneas del archivo
def generar_alfabeto(lineas):
    alfabeto = set()
    for linea in lineas:
        # Buscamos las líneas que comienzan con "alfabetoX:"
        match = re.match(r'^alfabeto(\d+): (.+)$', linea)
        if match:
            numero_alfabeto = match.group(1)
            contenido = match.group(2)
            # Si contiene "letras", agregamos todas las letras del alfabeto
            if contenido == 'letras':
                alfabeto.update(set(chr(i) for i in range(65, 91)))
                alfabeto.update(set(chr(i) for i in range(97, 123)))
            # Si contiene "digitos", agregamos los dígitos del 0 al 9
            elif contenido == 'digitos':
                alfabeto.update(set(str(i) for i in range(10)))
            # De lo contrario, agregamos las letras únicas
            else:
                alfabeto.update(set(contenido))
    return sorted(alfabeto)

# Función para obtener la expresión regular
def obtener_expresion(lineas):
    for linea in lineas:
        if linea.startswith("expresion:"):
            return re.sub(r'^expresion: (.+)$', r'\1', linea)

# Leer el archivo de entrada
archivo_entrada = 'expresiones.txt'
with open(archivo_entrada, 'r') as f:
    lineas = f.readlines()

# Generar el alfabeto
alfabeto = generar_alfabeto(lineas)

# Eliminar repeticiones en el alfabeto
alfabeto = sorted(set(alfabeto))

# Obtener la expresión regular
expresion_regular = obtener_expresion(lineas)

# Imprimir el resultado
print("Alfabeto:", ''.join(alfabeto))
print("Expresión regular:", expresion_regular)