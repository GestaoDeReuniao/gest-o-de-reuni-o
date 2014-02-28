import unittest
from should_dsl import should
from pontos import Pontos 
from questao import Questao


class QuestaoSpec(unittest.TestCase):
    
    def it_creates_questao(self):
         questao = Questao( 'motivo',[])
         questao.titulo |should| equal_to('motivo')
         questao.ponto  |should| equal_to([]) 

    def it_inserir_pontos(self):
          questao = Questao( 'motivo',[])
          ponto = Pontos ('jus')
          questao.inserir_ponto(ponto)
          (ponto in questao.ponto) |should| equal_to(True) 
