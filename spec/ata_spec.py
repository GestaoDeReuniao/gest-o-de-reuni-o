import unittest
from should_dsl import should
from ata import Ata
from questao import Questao

class AtaSpec(unittest.TestCase):


      def it_criar_ata(self):
           ata = Ata('cade', 'muito') 
           ata.titulo |should| equal_to('cade')
           ata.texto  |should| equal_to('muito') 
