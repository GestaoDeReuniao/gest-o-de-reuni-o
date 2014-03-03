import unittest
from should_dsl import should
from coordenador import Coordenador


class CoordenadorSpec(unittest.TestCase):


      def it_criar_coordenador(self):
           coordenador = Coordenador('123') 
           coordenador.login |should| equal_to('123')
