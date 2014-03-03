import unittest
from should_dsl import should
from convocacao import Convocacao
from participante import Participante
from reuniao import Reuniao
from ata import Ata
from palta import Palta
from local import Local 
from pessoa import Pessoa 





class ReuniaoSpec(unittest.TestCase):
    
      def it_criar_reuniao(self):
            palta = Palta('mais',[])  

            reuniao = Reuniao (palta, '123' , '89')
            reuniao.data |should| equal_to('123') 
            reuniao.hora |should| equal_to('89')
            reuniao.palta |should| equal_to(palta)   

 

      def  it_cadastrar_local (self):

            palta = Palta('mais',[])  
            local = Local('123', 'alberto')
            reuniao = Reuniao (palta, '123' , '89')
            reuniao.cadastrar_local(local)
            reuniao.local |should| equal_to(local) 


      def  it_retonar_estado(self):
            

            palta = Palta('mais',[])
            reuniao = Reuniao (palta, '123' , '89')
            reuniao.retornar_estado() |should| equal_to(1)  




      def it_alocar_pessoa(self):

            palta = Palta('mais',[])
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (palta , '123' , '89')
            convocacao = reuniao.alocar_pessoas(pessoa,'34')
            (convocacao in reuniao.convocados) |should| equal_to(True)



      def it_inserir_presentes(self):
            
            palta = Palta('mais',[])
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            reuniao = Reuniao (palta , '123' , '89')
            participacao = reuniao.inserir_presentes(pessoa,'12')
            (participacao in reuniao.presentes) |should| equal_to(True)   



      def it_confirmar_reuniao (self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            reuniao.confirmar_reuniao() 
            reuniao.retornar_estado() |should| equal_to(2)
      
      def it_cadastrar_ata(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')      
            ata = Ata('cade', 'muito') 
            reuniao.cadastrar_ata(ata)
            reuniao.ata |should| equal_to(ata) 
            reuniao.retornar_estado() |should| equal_to(3)



      def it_cancelar_reuniao(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            ata = Ata('cade', 'muito') 
            reuniao.cadastrar_ata(ata)
            reuniao.cancelar_reuniao()
            reuniao.retornar_estado() |should| equal_to(5)



      def it_aprovar_ata(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            ata = Ata('cade', 'muito') 
            reuniao.cadastrar_ata(ata)
            reuniao.aprovar_ata() 
            reuniao.retornar_estado() |should| equal_to(4)  




      def it_assinatura_de_ata(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            ata = Ata('cade', 'muito') 
            reuniao.cadastrar_ata(ata)
            reuniao.aprovar_ata() 
            reuniao.assinatura_de_ata()
            reuniao.retornar_estado() |should| equal_to(6)



      def it_desalocar_pessoa(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            convocacao = reuniao.alocar_pessoas(pessoa,'34')
            reuniao.desalocar_pessoa(pessoa)
            (convocacao in reuniao.convocados) |should| equal_to(False)
            convocacao.reuniao  |should| equal_to(None)



      def it_listar_ausentes(self):
            palta = Palta('mais',[])
            reuniao = Reuniao (palta , '123' , '89')
            pessoa = Pessoa('234','pedro','432','campos','rua','pdoisb')
            pessoa4 = Pessoa('234','pedro','432','campos','rua','pdoisb')
            pessoa2 = Pessoa('23','pedro','432','campo','ru','pdoisb')
            pessoa3 = Pessoa('2','pedro','432','camp','r','pdoisb') 
            reuniao.inserir_presentes(pessoa4,'12')
            reuniao.inserir_presentes(pessoa2,'12')
            reuniao.inserir_presentes(pessoa3,'12')
            reuniao.alocar_pessoas(pessoa,'34')
            reuniao.alocar_pessoas(pessoa4,'34')
            reuniao.alocar_pessoas(pessoa2,'34')
            reuniao.alocar_pessoas(pessoa3,'34')
            reuniao.listar_ausentes()
            (pessoa in reuniao.ausentes) |should| equal_to(True)



















































  












 
 






























      































