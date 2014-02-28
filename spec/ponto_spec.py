import unittest
from should_dsl import should
from pontos import Pontos 



class PontosSpec(unittest.TestCase):
      
      def it_criar_objeto(self): 
          ponto = Pontos('minha razao') 
          ponto.justificativa |should| equal_to('minha razao')
          
