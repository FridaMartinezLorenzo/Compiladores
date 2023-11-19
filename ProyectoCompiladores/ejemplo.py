import tkinter as tk
from tkinter import ttk

def create_labels(frame,canvas):
    k=0
    for i in range(100):
        label = tk.Label(frame, text=f"Label {i}",width=10)
       # label.grid(row=i, column=0, padx=10, pady=10)
        label.place(x=20,y=k)
        k+=35
        frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def show_scrollable_frame():
    new_window = tk.Toplevel(root)
    new_window.title("Scrollable Frame")

    canvas = tk.Canvas(new_window,bg="blue")
    canvas.place(x=0,y=500)

    scrollbar = ttk.Scrollbar(new_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.place(x=300,y=500,height=200)

    horizontal_scrollbar = ttk.Scrollbar(new_window, orient=tk.HORIZONTAL, command=canvas.xview)
    horizontal_scrollbar.set(0.0,0.9)
    horizontal_scrollbar.place(x=0,y=500,width=200)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    Button1=tk.Button(new_window,text="getLabel",command=lambda:create_labels(frame,canvas))
    Button1.place(x=30,y=50)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    

root = tk.Tk()
root.title("Scrollable Frame Example")

button = tk.Button(root, text="Mostrar Scrollable Frame", command=show_scrollable_frame)
button.pack(pady=10)

root.mainloop()



class Transition:
    symbol = ""
    next_state = -1
   
    def __init__(self, sy, st):
        self.symbol = sy
        self.next_state = st
   
    def getSymbol(self):
        return self.symbol
   
    def getState(self):
        return self.next_state
   
    def setSymbol(self, sy):
        self.symbol = sy
   
    def setState(self, st):
        self.next_state = st
       
    def __str__(self):
        return "Symbol: " + self.symbol + "Next State: " + str(self.next_state)+ "\n"
       


class State:
    def __init__(self):
        self.id = -1 #Id es el numero de estado
        self.next_state = []
        self.initial_state = False
        self.final_state = False
   
    def __init__(self, i, transition, ini, fin):
        self.id = i #Id es el numero de estado
        self.next_state = []
        if i != None:
            self.next_state.append(transition)
        self.initial_state = ini
        self.final_state = fin
   
    def getIniState(self):
        return self.initial_state
   
    def getFinalState(self):
        return self.final_state
   
    def getTransitions(self):
        return self.next_state
   
    def getId(self):
        return self.id
   
    def printTransitions(self):
        for s in self.next_state:
            print(s.getSymbol(), s.getState(), "\n")
   
    def setIniState(self, i):
        self.initial_state = i
   
    def setFinalState(self, f):
        self.final_state = f
   
    def setId(self, i):
        self.id = i
       
    def addTransition(self, t):
        self.next_state.append(t)
    
    def displayTransitions(self):
        i = 0
        for s in self.next_state:
            if (self.next_state[i] != None):
                print("To State: " + str(self.next_state[i].getState()) + " with Symbol: " + self.next_state[i].getSymbol())
                i+=1


               
    def __str__(self):
        return "Id: " + str(self.id) + " | Initial State: " + str(self.initial_state) + " | Final State: " + str(self.final_state) + "\n"
   


#Para la lista _______________________________________________________________________


# Definición de la clase Node


class Node:
    def __init__(self, state):
        self.state = state
        self.next = None


# Clase para la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None


    def append(self, state):
        new_node = Node(state)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def prepend(self, state):
        new_node = Node(state)
        new_node.next = self.head
        self.head = new_node


    def delete(self, state):
        if not self.head:
            return


        if self.head.state == state:
            self.head = self.head.next
            return


        current = self.head
        while current.next:
            if current.next.state == state:
                current.next = current.next.next
                return
            current = current.next


    def display(self):
        current = self.head
        while current:
            print(current.state)
            current.state.displayTransitions()
            print(end=" -> ")
            current = current.next
        print("None")


#____________________________________________________________________________________________________
#Se planea hacer una función por cada uno de los casos posibles
def SingleLetter(sym):
    List_SingleLetter = LinkedList()
    t = Transition(sym, 1)
    state1 = State(0, t, True, False)
    state2 = State(1,None, False, True)
    List_SingleLetter.append(state1)
    List_SingleLetter.append(state2)
   
    List_SingleLetter.display()
    return
