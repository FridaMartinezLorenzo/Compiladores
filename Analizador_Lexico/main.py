from Cargado_Datos import *
import re

class element_TokenTable:
    def __init__(self, lexema, token,nl):
        self.lexema = lexema
        self.token = token
        self.nlinea = nl

    def get_lexema(self):
        return self.lexema

    def get_token(self):
        return self.token
    
    def get_nlinea(self):
        return self.nlinea

    def set_lexema(self, lexema):
        self.lexema = lexema

    def set_token(self, token):
        self.token = token
    
    def set_nlinea(self, nl):
        self.nlinea = nl

    def __str__(self):
        return self.lexema + " " + self.token+ " " + str(self.nlinea)
    
#Función que desgloza el archivo de entrada 
def file_breakdown (lines, tokenList, symbolList_prog, ErrorList_prog):
    nline = 0
    for line in lines:
        nline+=1
        aux=""
        posNum = ""
        flag_string = False
        flag_found1 = flag_found_id = flag_found_num = flag_found_float=False
        flag_chkLex = False
        for char in line:

            # Si es espacio, y no es cadena, se activa la bandera para revisar el lexema
            print("flag_string: ",flag_string)
            if (char == ' ' or char == '\n' ) and flag_string == False: 
                flag_chkLex = True
            else:
                aux+=char
                pass

            # Si son comillas, revisar el estado de la bandera de cadena
            print("aux: ",aux)
            if char == '"' and flag_string == True: #Se encontro el fin de la cadena
                tokenList.append(element_TokenTable(aux, "varCadena", nline)) #Agregamos a la lista de tokens
                flag_string = False
                aux=""
                pass
            elif char == '"' and flag_string == False: #Es una cadena, se empieza a guardar y se enciende la bandera y asi si esta la bandera encendida esperamos el siguiente
                flag_string = True
                pass

            # Si es un solo caracter, revisa si es un símbolo
            if char in lista_simbolos and flag_string == False: #Es un simbolo
                if (flag_found_float == True):                  # Si ya se ha encontrado un punto antes en el número
                    tokenList.append(element_TokenTable(posNum, "nfloat", nline))
                    tokenList.append(element_TokenTable(char, char, nline))
                    flag_found_float = False
                    posNum = ""
                elif (posNum != "" and char != "."):            # Si hay un número entero posible, pero el símbolo no es un punto
                    tokenList.append(element_TokenTable(posNum, "nint", nline))
                    tokenList.append(element_TokenTable(char, char, nline))
                    posNum = ""
                elif (posNum == ""):
                    tokenList.append(element_TokenTable(char, char, nline)) #Agregamos a la lista de tokens
                aux = ""
                pass

            if flag_string == False:        # Si no es cadena, revisa el estado actual de aux y char...
                print(len(aux))
                print("Evaluacion de número entero")        # Busca si es un entero
                print("posNum: ", posNum)
                flag_found_num = es_numero(char)
                
                if posNum != "" and char == '.': #Evaluamos si posNum es diferente de vacio y existe un punto, porque entonces existe un flotante
                    print("Evaluacion de un flotante")
                    flag_found_float = True
                    posNum += char #Agregamos el punto al numero
                    pass
                
                if flag_found_num == True:
                    posNum += char
                    flag_found_num = False
                    pass
                elif flag_found_float == False:
                    if posNum != "" and char in lista_simbolos:     # Si hay un número entero posible
                        tokenList.append(element_TokenTable(posNum, "nint", nline))
                        posNum = ""
                
                if flag_found_float == True and char != '.' and flag_found_num == False:
                    if posNum != "" and char in lista_simbolos:     # Si hay un número flotante posible
                        tokenList.append(element_TokenTable(posNum, "nfloat", nline))
                        flag_found_float = False
                        posNum = ""

                print("Evaluacion de palabra reservada")    # Busca si es una palabra reservada
                flag_found1 = word_search(aux, nline, tokenList)
                print("flag_found1: ",flag_found1)
                if (flag_found1 == True):
                    flag_found1 = False
                    aux=""
                elif flag_chkLex == True:       # Si se detecta un espacio, puede haber una palabra por revisar
                    print("Evaluación de id")   # Busca si es un id
                    flag_found_id = es_id(aux, nline, tokenList)
                    if flag_found_id is True:
                        if (not BuscarSimbolo_ts(aux, symbolList_prog)):    # No existe en la tabla
                            symbolList_prog.append(element_SymbolTable(aux, "null", "null"))
                        flag_found_id = False
                    elif (len(aux)>0):
                        errorList_prog.append(nline, "Error: Lexema "+aux+" no definido")
                    flag_chkLex = False
                    aux = ""
                pass
                    



def word_search(word, nline, tokenList):
    if word in lista_pReservadas:
        tokenList.append(element_TokenTable(word, word, nline)) #Agregamos a la lista de tokens
        return 1
    return 0
    
def es_numero(cadena):
    try:
        int(cadena) # Intenta convertir la cadena a un entero
        return True
    except ValueError:
        return False # La conversión a entero falló, no es un número
    
def es_num_re(cadena):
    prueba = re.match(r'[0-9]', cadena)    # Cualquier repetición de números, pero sin un punto decimal al final
    if prueba is not None:
        return True
    return False

def es_float_re(cadena):
    prueba = re.match(r'[0-9]*\.[0-9]', cadena)   # Dos repeticiones de números, con un punto decimal entre ellas
    if prueba is not None:
        return True
    return False
    
def es_id(cadena, nline, tokenList):
    prueba = re.match('[a-zA-Z][a-zA-z0-9$_]*', cadena)
    if prueba is not None:
        tokenList.append(element_TokenTable(cadena, "id", nline))
        return True     # Encontró un nombre que empieza por letra, y contiene letras, números, $ ó _
    return False

def es_cad(cadena):
    prueba = re.match('".*"', cadena)
    if prueba is not None:
        return True     # Encontró una frase que está encerrada entre comillas dobles
    return False

def es_car(cadena):
    prueba = re.match("'.'", cadena)
    if prueba is not None:
        return True     # Encuentra un solo caracter entre comillas simples
    return False
    
    
#_____________________________________________________________________________________________________________________________________
# Leer el archivo de entrada


file = 'prueba.java'
with open(file, 'r') as f:
    lines_entry_file = f.readlines()

tokenList = []
file_breakdown(lines_entry_file, tokenList)   
for token in tokenList:
    print(token)
#word_search(cad, 1, tokenList)
#print(tokenList[0])