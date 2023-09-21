from pyformlang.fst import FST
import re

class Transducer(object):

    def __init__(self, name):
        self.name = name
        self.fst = self.init_transducer(name)
   