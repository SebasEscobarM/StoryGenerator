from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton as DFA,
    State as st,
    Symbol as sb,
)
from model.Transducer import Transducer as FST
import re


class Automaton(object):
    def __init__(self):
        self.names = self.initialize_names()
        self.states = self.set_up_states()
        self.final_states = self.set_up_final_states()
        self.automaton = self.set_up_automaton()
        self.regular_expressions = {}
        self.set_regular_expressions()

    def __str__(self) -> str:
        pass

    def set_names(self, names):
        for n in names:
            self.names.append(n)

    def set_states(self, states):
        for s in states:
            self.states.append(s)

    def accepts(self, input):
        return self.automaton.accepts(input)

    def to_regex(self):
        return self.automaton.to_regex()

    def to_dict(self):
        return self.automaton.to_dict()

    def is_final_state(self, state):
        return self.automaton.is_final_state(state)

    def is_start_state(self, state):
        return self.automaton.start_state == state

    def get_state(self, state_name):
        for pk in self.states:
            if pk.value == state_name:
                return pk

    def set_regular_expressions(self):
        nod_dict = self.to_dict()
        states = []
        for pk, val in nod_dict.items():
            for k in val.keys():
                states.append(k)

        regex_patterns = []
        for i in [
            re.compile(r".*(explorar|costa).*", re.IGNORECASE),
            re.compile(r".*(refugiar|bosque|buscar).*", re.IGNORECASE),
            re.compile(r".*(investigar|cueva).*", re.IGNORECASE),
            re.compile(r".*(avanzar|playa).*", re.IGNORECASE),
            re.compile(r".*(construir|choza).*", re.IGNORECASE),
            re.compile(r".*(noche|pasar|vela).*", re.IGNORECASE),
            re.compile(r".*(encontrar|mapa|antiguo).*", re.IGNORECASE),
            re.compile(r".*(despertar|criatura|durmiente).*", re.IGNORECASE),
            re.compile(r".*(descubrir|cofre|enterrado).*", re.IGNORECASE),
            re.compile(r".*(seguir|tribu|nativos).*", re.IGNORECASE),
            re.compile(r".*(encontrar|pistas|tesoro).*", re.IGNORECASE),
            re.compile(r".*(accionar|extraña|palanca|palmera).*", re.IGNORECASE),
            re.compile(r".*(investigar|ruido|extraño|matorrales).*", re.IGNORECASE),
            re.compile(r".*(tratar|sobrevivir|noche).*", re.IGNORECASE),
            re.compile(r".*(cavar|x|arena).*", re.IGNORECASE),
            re.compile(r".*(inspeccionar|antes).*", re.IGNORECASE),
            re.compile(r".*(huir|cueva).*", re.IGNORECASE),
            re.compile(r".*(comunicar|criatura).*", re.IGNORECASE),
            re.compile(r".*(quedar|solo).*", re.IGNORECASE),
            re.compile(r".*(cofre|llevar|ambos).*", re.IGNORECASE),
            re.compile(r".*(intentar|negociar|jefa).*", re.IGNORECASE),
            re.compile(r".*(escapar|nativos).*", re.IGNORECASE),
            re.compile(r".*noche.*", re.IGNORECASE),
            re.compile(r".*(día|dia).*", re.IGNORECASE),
            re.compile(
                r".*(continuar|busqueda|búsqueda|buscar|tesoro).*", re.IGNORECASE
            ),
            re.compile(r".*(isla|permanecer|ermitaño).*", re.IGNORECASE),
            re.compile(r".*(buscar|comida).*", re.IGNORECASE),
            re.compile(r".*(entrar|otro).*", re.IGNORECASE),
            re.compile(r".*(acuerdo|beneficio).*", re.IGNORECASE),
            re.compile(r".*robar.*", re.IGNORECASE),
            re.compile(r".*(esconder|embarcación|embarcacion).*", re.IGNORECASE),
            re.compile(r".*(correr|costa|desesperado|escapar).*", re.IGNORECASE),
        ]:
            regex_patterns.append(i)

        tuplas = list(zip(states, regex_patterns))
        self.regular_expressions = dict(tuplas)

    def initialize_names(self):
        names = {
            "Isla": "de los Secretos",
            "Playa": "de los Misterios",
            "Bosque": "de las Sombras",
            "Cueva": "de los Antiguos",
            "Choza": "Secreta",
            "Criatura": "Xelthor",
            "Lider": "Leilani",
            "Protagonista": "Silvanus",
        }
        return names

    def set_up_states(self):
        states = []

        for s in [
            st(f"Náufrago en la Isla {self.names['Isla']}"),  # q0
            st(f"Playa {self.names['Playa']}"),  # q1
            st(f"Bosque {self.names['Bosque']}"),  # q2
            st(f"Cueva {self.names['Cueva']}"),  # q3
            st(f"Orilla Despejada"),  # q4
            st(f"Choza {self.names['Choza']}"),  # q5
            st(f"Noche Tenebrosa"),  # q6
            st(f"Tesoro Enterrado"),  # q7
            st(f"Conversación con {self.names['Criatura']}"),  # q8
            st(f"Cofre del pasado"),  # q9
            st(f"Encuentro con los Nativos"),  # q10
            st(f"Ruinas Misteriosas"),  # q11
            st(f"Día Nuevo"),  # q12
            st(f"Afuera de la cueva {self.names['Cueva']}"),  # q13
            st(f"Acuerdo con los Nativos"),  # q14
            st(f"Fuga Desesperada"),  # q15
        ]:
            states.append(s)
        return states

    def set_up_final_states(self):
        final_states = []

        for fn in [
            st(
                f"Salvaje final: {self.names['Protagonista']} es atacado por animales salvaje"
            ),
            st(
                f"Devorado por la bestia: Era una bestia feroz, {self.names['Protagonista']} es devorado por ella"
            ),
            st(
                f"Regreso Triunfante: {self.names['Protagonista']} descubre el tesoro, es rescatado y regresa como héroe"
            ),
            st(
                f"Trampa mortal: {self.names['Protagonista']} Acciona accidentalmente una trampa mortal"
            ),
            st(
                f"Alianza inusual: {self.names['Protagonista']} Establece una comunicación inusual con {self.names['Criatura']} y logra salir de la isla en compañía de {self.names['Criatura']}"
            ),
            st(
                f"Ataque inesperado: {self.names['Protagonista']} es emboscado, atacado y asesinado por los nativos hostiles"
            ),
        ]:
            final_states.append(fn)

        return final_states

    def modify_name(self, subject, new_name):
        current_name = self.names[subject]
        fst = FST(current_name)
        fst.change_transducer(new_name)
        translated_name = fst.translate(current_name)
        if translated_name is not None:
            self.names[subject] = translated_name
        self.states = self.set_up_states()
        self.final_states = self.set_up_final_states()
        self.automaton = self.set_up_automaton()
        self.set_regular_expressions()

    def set_up_automaton(self):
        temp = DFA()
        q = self.states
        qf = self.final_states

        q0_q1 = sb(f"Explorar la costa".replace(" ", "_"))
        q0_q2 = sb(
            f"Buscar refugio en el bosque {self.names['Bosque']}".replace(" ", "_")
        )

        q1_q3 = sb(f"Investigar una cueva misteriosa".replace(" ", "_"))
        q1_q4 = sb(f"Avanzar por la playa {self.names['Playa']}".replace(" ", "_"))

        q2_q5 = sb(f"Construir una choza".replace(" ", "_"))
        q2_q6 = sb(f"Pasar la noche en vela".replace(" ", "_"))

        q3_q7 = sb(f"Encontrar un mapa antiguo".replace(" ", "_"))
        q3_q8 = sb(
            f"Despertar a una criatura durmiente llamada {self.names['Criatura']}".replace(
                " ", "_"
            )
        )

        q4_q9 = sb(f"Descubrir un cofre enterrado".replace(" ", "_"))
        q4_q10 = sb(
            f"Seguir a una tribu de nativos liderada por la jefa {self.names['Lider']}".replace(
                " ", "_"
            )
        )

        q5_q11 = sb(f"Encontrar pistas sobre el tesoro".replace(" ", "_"))
        q5_qfin1 = sb(f"Accionar una extraña palanca en una palmera".replace(" ", "_"))

        q6_qfin2 = sb(
            f"Investigar un ruido extraño proveniente de los matorrales".replace(
                " ", "_"
            )
        )
        q6_q12 = sb(
            f"Tratar de sobrevivir a la noche desde un único punto".replace(" ", "_")
        )

        q7_qfin3 = sb(f"Cavar en la X que hay en la arena".replace(" ", "_"))
        q7_qfin4 = sb(f"Inspeccionar el lugar antes de cavar en la X".replace(" ", "_"))

        q8_q13 = sb(f"Huir de la cueva {self.names['Cueva']}".replace(" ", "_"))
        q8_qfin5 = sb(
            f"Intentar comunicarte con {self.names['Criatura']}".replace(" ", "_")
        )

        q9_qfin3 = sb(f"Quedarse solo con el tesoro".replace(" ", "_"))
        q9_qfin4 = sb(f"Llevarse el tesoro y el cofre".replace(" ", "_"))

        q10_q14 = sb(
            f"Intentar negociar con la jefa {self.names['Lider']}".replace(" ", "_")
        )
        q10_q15 = sb(f"Escapar sigilosamente de los nativos".replace(" ", "_"))

        q11_qfin1 = sb(f"Explorar las ruinas de noche".replace(" ", "_"))
        q11_qfin6 = sb(f"Explorar las ruinas de día".replace(" ", "_"))

        q12_qfin3 = sb(f"Continuar la búsqueda del misterioso tesoro".replace(" ", "_"))
        q12_qfin1 = sb(
            f"Permanecer en la isla {self.names['Isla']} como ermitaño llamado {self.names['Protagonista']}".replace(
                " ", "_"
            )
        )

        q13_qfin3 = sb(
            f"Buscar comida alrededor de la cueva {self.names['Cueva']}".replace(
                " ", "_"
            )
        )
        q13_qfin4 = sb(
            f"Tratar de entrar por el otro lado de la cueva {self.names['Cueva']}".replace(
                " ", "_"
            )
        )

        q14_qfin3 = sb(
            f"Llegar a un acuerdo beneficioso con la jefa {self.names['Lider']}".replace(
                " ", "_"
            )
        )
        q14_qfin6 = sb(f"Tratar de robar a los nativos".replace(" ", "_"))

        q15_qfin3 = sb(f"Esconderse en una embarcación".replace(" ", "_"))
        q15_qfin6 = sb(
            f"Correr hasta la costa en un intento desesperado por escapar".replace(
                " ", "_"
            )
        )

        temp.add_transitions(
            [
                (q[0], q0_q1, q[1]),
                (q[0], q0_q2, q[2]),
                (q[1], q1_q3, q[3]),
                (q[1], q1_q4, q[4]),
                (q[2], q2_q5, q[5]),
                (q[2], q2_q6, q[6]),
                (q[3], q3_q7, q[7]),
                (q[3], q3_q8, q[8]),
                (q[4], q4_q9, q[9]),
                (q[4], q4_q10, q[10]),
                (q[5], q5_q11, q[11]),
                (q[5], q5_qfin1, qf[0]),
                (q[6], q6_qfin2, qf[1]),
                (q[6], q6_q12, q[12]),
                (q[7], q7_qfin3, qf[2]),
                (q[7], q7_qfin4, qf[3]),
                (q[8], q8_q13, q[13]),
                (q[8], q8_qfin5, qf[4]),
                (q[9], q9_qfin3, qf[2]),
                (q[9], q9_qfin4, qf[3]),
                (q[10], q10_q14, q[14]),
                (q[10], q10_q15, q[15]),
                (q[11], q11_qfin1, qf[0]),
                (q[11], q11_qfin6, qf[5]),
                (q[12], q12_qfin3, qf[2]),
                (q[12], q12_qfin1, qf[0]),
                (q[13], q13_qfin3, qf[2]),
                (q[13], q13_qfin4, qf[3]),
                (q[14], q14_qfin3, qf[2]),
                (q[14], q14_qfin6, qf[5]),
                (q[15], q15_qfin3, qf[2]),
                (q[15], q15_qfin6, qf[5]),
            ]
        )

        temp.add_start_state(q[0])
        for st in qf:
            temp.add_final_state(st)

        return temp
