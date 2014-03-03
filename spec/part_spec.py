import unittest
from should_dsl import should
from part import Part


class PartSpec(unittest.TestCase):


      def it_criar_part(self):
           part = Part('123') 
           part.tempo |should| equal_to('123')
