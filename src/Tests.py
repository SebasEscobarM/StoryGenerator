import unittest
from model import Transducer, Automaton, Grammar
from pyformlang.finite_automaton import State as st


class SystemUnitTest(unittest.TestCase):
    def test_change_name(self):
        tr = Transducer.Transducer("Pepe")

        tr.change_transducer("Roberto")
        r1 = tr.replace_name("Pepe")
        self.assertEqual(r1, "Roberto")

        tr.change_transducer("Ana")
        r2 = tr.replace_name("Pepe?")
        self.assertEqual(r2, "Ana?")

        tr.change_transducer("Juan Alejandro")
        r3 = tr.replace_name(
            "Un dia Pepe iba de camino a su casa tranquilo cuando escucho: ¡Pepe!. Pepe giro la cabeza buscando quien lo llamaba."
        )
        self.assertEqual(
            r3,
            "Un dia Juan Alejandro iba de camino a su casa tranquilo cuando escucho: ¡Juan Alejandro!. Juan Alejandro giro la cabeza buscando quien lo llamaba.",
        )

    def test_grammar(self):
        gr = Grammar.Grammar()
        aut = gr.automaton

        w = gr.generate_rd_story()
        self.assertTrue(aut.accepts(w))

        w1 = gr.generate_rd_story()
        self.assertTrue(aut.accepts(w1))

        w2 = gr.generate_rd_story()
        self.assertTrue(aut.accepts(w2))

    def test_automaton(self):
        aut = Automaton.Automaton()
        aut.states = []
        aut.set_states([st("Estado 1"), st("Estado 2"), st("Estado 3")])
        self.assertEqual(aut.states, [st("Estado 1"), st("Estado 2"), st("Estado 3")])

        self.assertTrue(aut.contains_state(aut.get_state("Estado 1")))


if __name__ == "__main__":
    unittest.main()
