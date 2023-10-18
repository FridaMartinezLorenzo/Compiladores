
#Definimos las clases que utilizaremos para la construccion del automata de thompson        
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
        
    def __str__(self):
        return "Id: " + str(self.id) + " Initial State: " + str(self.initial_state) + " Final State: " + str(self.final_state) + "\n"
    

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
            print(current.state, end=" -> ")
            current = current.next
        print("None")

# Creating a linked list
my_linked_list = LinkedList()

#Creating and object
t1 = Transition("a", 1)
s = State(0,t1, True, False)
r = State(1, t1, False, True)
# Appending elements to the linked list
my_linked_list.append(s)
my_linked_list.append(r)

# Displaying the linked list
my_linked_list.display()

    #Se planea hacer una función por cada uno de los casos posibles
    