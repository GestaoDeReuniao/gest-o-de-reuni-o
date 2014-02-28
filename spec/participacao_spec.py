import unittest
from should_dsl import should
from pessoa import Pessoa
from participante import Participante

class ParticipanteSpec(unittest.TestCase):




      def it_criar_participante(self):
           pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')           
           participante = Participante(pessoa, '21', 'muitolega')
           participante.data |should| equal_to('21')
           participante.pessoa  |should| equal_to(pessoa) 
           participante.contribuicao |should| equal_to ('muitolega')  

 
