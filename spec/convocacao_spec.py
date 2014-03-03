import unittest
from should_dsl import should
from convocacao import Convocacao
from pessoa import Pessoa
from reuniao import Reuniao
from participante import Participante


class ConvocacaoSpec(unittest.TestCase):
   
       def it_criar_convocacao(self):
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (None , '123' , '89')


            convocacao = Convocacao( pessoa, '45', reuniao)
            convocacao.pessoa |should| equal_to(pessoa)
            convocacao.data   |should| equal_to('45')
            convocacao.reuniao|should| equal_to(reuniao)
            convocacao.estado |should| equal_to(1)
       def it_desfazer_convocacao(self):
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (None , '123' , '89')


            convocacao = Convocacao( pessoa, '45', reuniao)
            convocacao.desfazer_convocacao(None)
            convocacao.reuniao |should| equal_to(None)
            convocacao.estado |should| equal_to(3) 
       def it_confirmar(self):
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (None , '123' , '89')


            convocacao = Convocacao( pessoa, '45', reuniao)
            convocacao.confirmar()
            convocacao.estado |should| equal_to(2)
            

       def it_retorna_estado(self):
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (None , '123' , '89')


            convocacao = Convocacao( pessoa, '45', reuniao)
            convocacao.confirmar()
            convocacao.retorna_estado() |should| equal_to(2)



       def it_desalocar(self):
        
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (None , '123' , '89')


            convocacao = Convocacao( pessoa, '45', reuniao)
            convocacao.confirmar()
            convocacao.desalocar('atraso')
            convocacao.motivo  |should| equal_to('atraso')
            convocacao.retorna_estado() |should| equal_to(3)
            convocacao.reuniao |should| equal_to(None)
             

               
       def it_confirmar_presenca(self):
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao ('casa' , '123' , '89')


            
            pessoa4 = Pessoa('234','pedro','432','campos','rua','pdoisb')
            pessoa2 = Pessoa('23','pedro','432','campo','ru','pdoisb')
            pessoa3 = Pessoa('2','pedro','432','camp','r','pdoisb')
           
            
            convocacao = reuniao.alocar_pessoas(pessoa,'34')
            convocacao.confirmar()
            reuniao.inserir_presentes(pessoa, '12')
            reuniao.inserir_presentes(pessoa4, '231')
             
            (convocacao in reuniao.convocados) |should| equal_to(True)  
            convocacao.confirmar_presenca()
            convocacao.estado |should| equal_to(4) 
            

















   
  
               
      

