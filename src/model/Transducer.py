from pyformlang.fst import FST
import re

class Transducer(object):

    def __init__(self, name):
        self.name = name
        self.fst = self.init_transducer(name)
   
    def __init__(self, name):
        self.name = name
        self.fst = self.init_transducer(name)
    
    def get_fst(self):
        return self.fst
    
    def translate(self, name):
        output = None
        try:
            output = "".join(list(self.fst.translate(name))[0])
        except Exception as e:
            print(f"Something went wrong: {e}")
        return output

    def init_transducer(self, name):
        nt = FST()
        n = len(name)
        for i in range (0,n):
            nt.add_transition(chr(i+48) ,name[i],chr(i+49),[name[i]])
        nt.add_start_state('0')
        nt.add_final_state(chr(n+48))
        return nt
    
    def change_transducer(self, nwName):
        name = self.name
        nt = FST()
        if len(name)>=len(nwName):
            n=len(name)
            for i in range(n):
                if i>=len(nwName):
                    nt.add_transition(chr(i+48) ,name[i],chr(i+49),[''])
                else:
                    nt.add_transition(chr(i+48),name[i],chr(i+49),[nwName[i]])
        else:
            n=len(nwName)
            for i in range(n):
                if i>=len(name):
                    nt.add_transition(chr(i+48),'epsilon',chr(i+49),[nwName[i]])
                else:
                    nt.add_transition(chr(i+48),name[i],chr(i+49),[nwName[i]])
        nt.add_start_state('0')
        nt.add_final_state(chr(n+48))

        self.fst = nt

    def replace_name(self, texto):
        # Definir una expresión regular para encontrar "Pepe" con cualquier puntuación o espacio alrededor
        name = self.name
        patron = rf'\b{name}\b'

        cont=True
            
        # Iterar a través de las ocurrencias y reemplazarlas con el nombre nuevo
        while cont:
            oc=re.search(patron,texto)
            if oc:
                inicio, fin = oc.start(), oc.end()
                nombre = texto[inicio:fin]
                nombre_nuevo = "".join(list(self.fst.translate(nombre))[0])
                texto = texto[:inicio] + nombre_nuevo + texto[fin:]
            else:
                cont=False
        
        return texto