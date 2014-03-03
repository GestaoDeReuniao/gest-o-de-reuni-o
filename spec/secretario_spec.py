import unittest
from should_dsl import should
from secretario import Secretario


class SecretarioSpec(unittest.TestCase):


      def it_criar_secretario(self):
           secretario = Secretario('123') 
           secretario.login |should| equal_to('123')
