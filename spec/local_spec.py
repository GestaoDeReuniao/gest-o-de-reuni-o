import unittest
from should_dsl import should
from local import Local

class LocalSpec(unittest.TestCase):


      def it_criar_ata(self):
           local = Local('123', 'alberto') 
           local.endereco |should| equal_to('123')
           local.nome  |should| equal_to('alberto') 
