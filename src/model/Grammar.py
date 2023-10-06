from pyformlang.finite_automaton import DeterministicFiniteAutomaton as DFA, State as st
from pyformlang.cfg import CFG
import random as rd


class Grammar(object):

    def __init__(self):
            self.automaton = self.init_automaton()
            self.grammar = self.init_grammar()


    def generate_rd_story(self):
        lst=self.grammar.get_words(5)
        li = []
        for i in lst:
            w=""
            for t in i:
                w+=t.to_text()
            li.append(w)

        li=list(filter(self.automaton.accepts,li))
        word=rd.choice(li)
        return word
        



    def init_grammar(self):
        stGen=CFG.from_text("""
            S -> A A A B B
            A -> a | b
            B -> a | b | epsilon
        """)
        return stGen


    def init_automaton(self):
        # States definition
        q0 = "q0"  # Llegada a la Isla Perdida (q0)
        q1 = "q1"  # Explorar la costa (q1)
        q2 = "q2"  # Buscar refugio en el bosque (q2)
        q3 = "q3"  # Dentro de la cueva (q3)
        q4 = "q4"  # Siguiendo la playa (q4)
        q5 = "q5"  # Construir una choza (q5)
        q6 = "q6"  # Pasar la noche en vela (q6)
        q7 = "q7"  # Siguiendo el mapa antiguo (q7)
        q8 = "q8"  # Criatura durmiente (q8)
        q9 = "q9"  # Abriendo el cofre (q9)
        q10 = "q10"  # Capturado por nativos hostiles (q10)
        q11 = "q11"  # Pistas sobre el tesoro (q11)
        q12 = "q12"  # Sobrevivir la noche (q12)
        q13 = "q13"  # Huir de la cueva (q13)
        q14 = "q14"  # Negociar con los nativos (q14)
        q15 = "q15"  # Escapar de los nativos (q15)

        # Final states
        qf1 = st("qf1")  # Atacado por animales salvajes
        qf2 = st("qf2")  # Experiencia aterradora en la noche
        qf3 = st("qf3")  # Descubres el tesoro y regresas como un héroe
        qf4 = st("qf4")  # Encuentras un destino desafortunado o trágico
        qf5 = st("qf5")  # Estableces una comunicación inusual con la criatura durmiente
        qf6 = st("qf6") #Emboscado y asesinado por los nativos


        # DFA definition
        nod = DFA()

        # Transitions
        nod.add_transitions([
        # q0. | 1. Llegada a la Isla Perdida
        (q0,"a",q1),   
        (q0,"b",q2), 

        # q1. | 2. Explorar la costa
        (q1,"a",q3),  
        (q1,"b",q4),  

        # q2. | 3. Buscar refugio en el bosque
        (q2,"a",q5), 
        (q2,"b",q6),  

        # q3. | 4. Dentro de la cueva
        (q3,"a",q7), 
        (q3,"b",q8),  

        # q4. | 5. Siguiendo la playa
        (q4,"a",q9),  
        (q4,"b",q10),  

        # q5. | 6. Construir una choza
        (q5,"a",q11), 
        (q5,"b",qf1),  

        # q6. | 7. Pasar la noche en vela
        (q6,"a",qf2), 
        (q6,"b",q12), 

        # q7. | 8. Siguiendo el mapa antiguo
        (q7,"a",qf3),  
        (q7,"b",qf4), 

        # q8. | 9. Criatura durmiente
        (q8,"a",q13),  
        (q8,"b",qf5),  

        # q9. | 10. Abriendo el cofre
        (q9,"a",qf3),  
        (q9,"b",qf4),  

        # q10. | 11. Capturado por nativos hostiles
        (q10,"a",q14),
        (q10,"b",q15),

        # q11. | 12. Pistas sobre el tesoro
        (q11,"a",qf3), 
        (q11,"b",qf6),  

        # q12. | 13. Sobrevivir la noche
        (q12,"a",qf3),  
        (q12,"b",qf1), 

        # q13. | 14. Huir de la cueva
        (q13,"a",qf3),  
        (q13,"b",qf4), 

        # q14. | 15. Negociar con los nativos
        (q14,"a",qf3),  
        (q14,"b",qf6), 

        # q15. | 16. Escapar de los nativos
        (q15,"a",qf3),  
        (q15,"b",qf6)   
        ])

        # Start state
        nod.add_start_state(q0)

        # Final states
        nod.add_final_state(qf1)
        nod.add_final_state(qf2)
        nod.add_final_state(qf3)
        nod.add_final_state(qf4)
        nod.add_final_state(qf5)
        nod.add_final_state(qf6)

        return nod
