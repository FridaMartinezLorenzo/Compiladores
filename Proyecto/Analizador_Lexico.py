from Cargado_Datos_AL import *
from tkinter import *
import lexico as lx
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import re

#Añadimos la parte grafica
def Analizador_Lexico():
    font1=("Times New Roman",12)
    arrLabels=[]
    lexWindow=Toplevel()
    lexWindow.state("zoomed")
    lexWindow.title("Analizador Lexico")
    lexWindow.config(bg="#363062")
    lineas_entrada = []

    archivoL=Label(lexWindow,text="Selecciona un archivo .java",width=30,font=font1)
    archivoL.place(x=20,y=25)

    archivoButton=Button(lexWindow,text="Abrir archivo",width=20,command=lambda:abrirArchivo(lexWindow,lineas_entrada),bg="#F99417" ,font=font1)
    archivoButton.place(x=350,y=20)

    canvas=Canvas(lexWindow,width=1500,height=900)
    canvas.place(x=0,y=120)

    def on_arrow_key(event):
            if event.keysym == "Left":
                canvas.xview_scroll(-1, "units")
            elif event.keysym == "Right":
                canvas.xview_scroll(1, "units")
            #canvas.config(scrollregion=canvas.bbox("all"))    

    def on_arrow_key_v(event):
         if event.keysym == "Up":
             canvas.yview_scroll(-1, "units")
         elif event.keysym == "Down":
             canvas.yview_scroll(1, "units")
         #canvas.config(scrollregion=canvas.bbox("all"))
    
    scrollbar=ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.set(0.0, 1.0)
    scrollbar.place(x=5, y=50, height=300)

    horizontal_scrollbar = ttk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    horizontal_scrollbar.set(0.0,1.0)
    horizontal_scrollbar.place(x=0,y=0,width=300)

    tabla=Frame(canvas,width=1470,height=300)
    canvas.create_window((100, 50), window=tabla, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    
    ttokenButton=Button(lexWindow,text="Tabla Tokens",width=20,command=lambda:MostrarTablaTokens(tabla,canvas,lexWindow,arrLabels,lineas_entrada),bg="#83A2E8" ,font=font1)
    ttokenButton.place(x=350,y=70)
        
    terroresButton=Button(lexWindow,text="Tabla Errores",width=20,command=lambda:MostrarTablaErrores(tabla,canvas,lexWindow,arrLabels),bg="#83A2E8" ,font=font1)
    terroresButton.place(x=550,y=70)
    
    tsimbolosButton=Button(lexWindow,text="Tabla Símbolos",width=20,command=lambda:MostrarTablaSimbolos(tabla,canvas,lexWindow,arrLabels),bg="#83A2E8" ,font=font1)
    tsimbolosButton.place(x=750,y=70)
    

    def on_mousewheel(event):
         canvas.yview_scroll(-1 * (event.delta // 120), "units")
    
    cleanButton=Button(lexWindow,text="Limpiar",font=font1,bg="#F99417",command=lambda:cleanTable(tabla,arrLabels))
    cleanButton.place(x=550,y=20)
    tabla.update_idletasks()
    #canvas.config(scrollregion=canvas.bbox("all"))
    canvas.bind("<MouseWheel>", on_mousewheel)
    canvas.bind_all("<KeyPress-Left>", on_arrow_key)
    canvas.bind_all("<KeyPress-Right>", on_arrow_key)
    canvas.bind_all("<KeyPress-Up>", on_arrow_key_v)
    canvas.bind_all("<KeyPress-Down>", on_arrow_key_v)

def cleanTable(tabla,arrLabels):
    for widget in tabla.winfo_children():
        widget.destroy()
    for widget in arrLabels:
        widget.destroy()
    arrLabels.clear()#Limpiar la lista
    
    
def MostrarTablaTokens(tabla,canvas,lexWindow,arrLabels,lines_entry_file):
    font1=("Times New Roman",11)
    columnas_titulos = ['Lexema', 'Token', '# Linea']
    columna=1
    lista_Tokens = []
    file_breakdown(lines_entry_file, lista_Tokens)   
    for titulo in columnas_titulos:
        col=Label(tabla,text=titulo,width=20,borderwidth=1, relief="solid",font=font1)
        col.grid(row=0,column=columna)
        arrLabels.append(col)
        columna+=1
   
    tabla.update_idletasks()
    #canvas.config(scrollregion=canvas.bbox("all"))
    numElementos=len(lista_Tokens)#Numero de estados
    i = 1
    if numElementos > 0:
        while i < numElementos:
            nodo  = lista_Tokens[i]
            lexema_nodo = nodo.get_lexema()
            token_nodo  = nodo.get_token()
            nlinea_nodo = nodo.get_nlinea()

            celda_lexema = Label(tabla,text=lexema_nodo,width=20,borderwidth=1, relief="solid",font=font1)
            celda_lexema.grid(row=i,column=1)

            celda_token = Label(tabla,text=token_nodo,width=20,borderwidth=1, relief="solid",font=font1)
            celda_token.grid(row=i,column=2)

            celda_sym = Label(tabla,text=nlinea_nodo,width=20,borderwidth=1, relief="solid",font=font1)
            celda_sym.grid(row=i,column=3)

            i+=1
        #canvas.config(scrollregion=canvas.bbox("all"))
    else:
        lexWindow.grab_set()
        messagebox.showerror("Error","Elige un archivo valido")
        lexWindow.grab_release()
        
    
    

def abrirArchivo(lexWindow, lineas_entrada):
    lexWindow.grab_set()
    direccionArchivo=filedialog.askopenfilename(initialdir=r"C:\Users\Documents\Compiladores",title="Abrir",filetypes=(("java","*.java"),))
    try:
        with open(direccionArchivo, 'r') as archivo:
            # Modificar directamente la lista lineas_entrada
            lineas_entrada.clear()  # Limpiar la lista actual
            lineas_entrada.extend(archivo.readlines())  # Extender la lista con las nuevas líneas
            print(direccionArchivo)
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
    
    lexWindow.grab_release()








#__________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________

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
def file_breakdown (lines, tokenList):
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
            if char in lista_simbolos and flag_string == False and posNum == "": #Es un simbolo
                tokenList.append(element_TokenTable(char, char, nline)) #Agregamos a la lista de tokens
                aux=""
                pass
            if flag_string == False:
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
                    if posNum != "" and char in lista_simbolos:     # Si hay un número posible, y el último char es un símbolo
                        tokenList.append(element_TokenTable(posNum, "nint", nline))

                        tokenAux = tokenList[len(tokenList)-2]          # Intercambia posiciones del símbolo y el número, para que estén bien ordenados
                        tokenList[len(tokenList)-2] = tokenList[len(tokenList)-1]
                        tokenList[len(tokenList)-1] = tokenAux
                        posNum = ""
                
                if flag_found_float == True and char != '.' and flag_found_num == False:
                    if posNum != "" and char in lista_simbolos:     # Si hay un número posible, y el último char es un símbolo
                        tokenList.append(element_TokenTable(posNum, "nfloat", nline))
                        flag_found_float = False

                        tokenAux = tokenList[len(tokenList)-2]          # Intercambia posiciones del símbolo y el número, para que estén bien ordenados
                        tokenList[len(tokenList)-2] = tokenList[len(tokenList)-1]
                        tokenList[len(tokenList)-1] = tokenAux
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
                        flag_found_id = False
                        aux = ""
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
    
def es_nint_re(cadena):
    prueba = re.match(r'[0-9]*(?!\.)', cadena)    # Cualquier repetición de números, pero sin un punto decimal al final
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
