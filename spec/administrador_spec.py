import unittest
from should_dsl import should
from administrador import Administrador


class AdministradorSpec(unittest.TestCase):


      def it_criar_Administrador(self):
           administrador = Administrador('123') 
           administrador.senha |should| equal_to('123')
