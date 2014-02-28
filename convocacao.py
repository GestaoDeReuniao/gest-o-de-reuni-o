#coding:utf-8


class Convocacao:
      ALOCADO = 1 
      DESALOCADO = 3
      PRESENTE = 4
      AUSENTE = 5
      CONFOCADO =2              
      
      def __init__ (self,pessoa,data, reuniao):
            self.pessoa = pessoa 
            self.data = data 
            self.estado = self.ALOCADO 
            self.reuniao = reuniao

      
        
      def retorna_estado(self):
          return self.estado  
      def desfazer_convocacao(self,reuniao):
          self.reuniao = reuniao  
          self.estado = DESALOCADO
      def desalocar(self, motivo):
          if estado ==  2 :
             self.motivo = motivo 
             self.estado = DESALOCADO
             self.desfazer_convocacao(reuniao) 
             
      def confirmar_presenca(self):
          if self.estado == 2  :
              for variavel in self.reuniao.presentes :
                  if self == variavel:
                     self.estado = PRESENTE      
              if self.estado != 4 :
                  self.estado = AUSENTE  
            
