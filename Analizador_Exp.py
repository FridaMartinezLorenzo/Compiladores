class State:
    def _init_(self, label=None):
        self.transitions = {}
        self.epsilon_transitions = []
        self.label = label
        self.accepting = False

class NFA:
    def _init_(self, start_state, accept_state):
        self.start_state = start_state
        self.accept_state = accept_state

def thompson(expr):
    stack = []
    
    for char in expr:
        if char == '(':
            stack.append('(')
        elif char == ')':
            nfa_stack = []
            while stack and stack[-1] != '(':
                nfa_stack.append(stack.pop())
            stack.pop()  # Remove '('
            for op in nfa_stack:
                if op == '|':
                    nfa2 = stack.pop()
                    nfa1 = stack.pop()
                    start_state = State()
                    accept_state = State()
                    start_state.epsilon_transitions.append(nfa1.start_state)
                    start_state.epsilon_transitions.append(nfa2.start_state)
                    nfa1.accept_state.epsilon_transitions.append(accept_state)
                    nfa2.accept_state.epsilon_transitions.append(accept_state)
                    stack.append(NFA(start_state, accept_state))
                elif op == '.':
                    nfa2 = stack.pop()
                    nfa1 = stack.pop()
                    nfa1.accept_state.epsilon_transitions.append(nfa2.start_state)
                    stack.append(NFA(nfa1.start_state, nfa2.accept_state))
                else:
                    accept_state = State()
                    start_state = State()
                    start_state.transitions[char] = accept_state
                    stack.append(NFA(start_state, accept_state))
        elif char == '|':
            stack.append('|')
        else:
            accept_state = State()
            start_state = State()
            start_state.transitions[char] = accept_state
            stack.append(NFA(start_state, accept_state))

        while len(stack) > 1:
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept_state.epsilon_transitions.append(nfa2.start_state)
            stack.append(NFA(nfa1.start_state, nfa2.accept_state))
        
        return stack[0]

def epsilon_closure(states):
    closure = set()
    stack = list(states)
    while stack:
        state = stack.pop()
        if state not in closure:
            closure.add(state)
            stack.extend(state.epsilon_transitions)
    return closure

def move(states, char):
    move_states = set()
    for state in states:
        if char in state.transitions:
            move_states.add(state.transitions[char])
    return epsilon_closure(move_states)

def match(nfa, input_string):
    current_states = epsilon_closure({nfa.start_state})
    
    for char in input_string:
        current_states = move(current_states, char)
    
    return nfa.accept_state in current_states

# Ejemplo de uso
expr = "(a|b)*abb"
nfa = thompson(expr)

input_strings = ["", "a", "b", "ab", "abb", "aaabbb", "ababab", "aab", "abba"]
for string in input_strings:
    if match(nfa, string):
        print(f"'{string}' es una coincidencia")