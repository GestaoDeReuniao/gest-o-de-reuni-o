import unittest
from should_dsl import should
from palta import Palta
from questao import Questao

class PaltaSpec(unittest.TestCase):




      def it_criar_palta(self):
           palta = Palta('mais', questao =[])
           palta.titulo |should| equal_to('mais')
           palta.questao  |should| equal_to([]) 


      def it_inserir_questao(self):
           questao = Questao( 'motivo',[])
           palta = Palta ( 'mais', [])
           palta.inserir_questao(questao)
           (questao in palta.questao) |should| equal_to(True) 
