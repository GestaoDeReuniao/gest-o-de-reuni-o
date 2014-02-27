import unittest
from should_dsl import should
from pessoa import Pessoa

#matricula,nome,cpf,cidade,endereco,email,
class PessoaSpec(unittest.TestCase):




      def it_criar_pessoa(self):
           pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
           pessoa.matricula |should| equal_to('234')
           pessoa.nome |should| equal_to('pedro') 
           pessoa.cpf |should| equal_to('432')  
           pessoa.cidade |should| equal_to('campos')
           pessoa.endereco |should| equal_to('rua')
           pessoa.email |should| equal_to('pdoisb')
