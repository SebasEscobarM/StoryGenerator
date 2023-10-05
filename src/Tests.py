import unittest
from model import Transducer, Automaton, Grammar

class SystemUnitTest(unittest.TestCase):

    def test_change_name(self):
        tr=Transducer.Transducer("Pepe")

        tr.change_transducer("Roberto")
        r1=tr.replace_name("Pepe")
        self.assertEqual(r1, "Roberto")

        tr.change_transducer("Ana")
        r2=tr.replace_name("Pepe?")
        self.assertEqual(r2,"Ana?")

        tr.change_transducer("Juan Alejandro")
        r3=tr.replace_name("Un dia Pepe iba de camino a su casa tranquilo cuando escucho: ¡Pepe!. Pepe giro la cabeza buscando quien lo llamaba.")
        self.assertEqual(r3,"Un dia Juan Alejandro iba de camino a su casa tranquilo cuando escucho: ¡Juan Alejandro!. Juan Alejandro giro la cabeza buscando quien lo llamaba.")

          
        

if __name__ == '__main__':
    unittest.main()