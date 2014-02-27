#coding:utf-8
class Reuniao:
      PREPARACAO = 1 
      CONFIRMADA = 2
      AGUARDANDO_APROVACAO_ATA = 3
      AGUARDANDO_ASSINATURA_ATA = 4
      CANCELADA = 5
      ATA_ASSINADA = 6

      def __init__(self,palta,data, hora):
                 if palta != None:  
                      self.palta = palta
                      self.data = data
                      self.hora = hora
                      self.presentes = [] 
                      self.convocacao = []
                      
                      self.estado = PREPARACAO

      
                 

      def cadastrar_local (self,local):
                 self.local = local    
      
      def alocar_pessoas(self,pessoa,data):
                 
                 convocacao = Convocacao(pessoa,data,self)
                 self.convocacao.append(convocacao)
                 
                                                


      def inserir_presentes(self,pessoa, data):

                 participante = Participante (pessoa, data)  
                 self.presentes.append(presente) 
      def confirmar_reuniao (self):
                 if self.estado == 1:  
                      self.estado = CONFIRMADO 


      def cadastrar_ata (self,ata):
                  self.ata = ata
                  self.estado = AGUARDANDO_APROVACAO_ATA  

      def cancelar_reuniao(self):
                  if self.estado <4 :
                       self.estado = CANCELADO  

      def aprovar_ata(self):
                  if self.estado == 4:
                       self.estado = AGUARDANDO_ASSINATURA_ATA                  
                       
   
      def assinatura_de_ata(self):

                   if self.estado == 5:
                       self.estado = ATA_ASSINADA 

      def desalocar_pessoa(self,pessoa):
                   for variavel in self.convocacao:   
                        if variavel.convocacao.pessoa == pessoa: 
                               variavel.convocacao.desfazer_convocacao(None)
                               self.convocacao.remove(variavel)  


      def retonar_estado(self):
                   return self.estado 
      def retonar_ausentes(self):
                   self.ausentes = []  
                   for variavel in self.convocacao:
                        if variavel.estado == 2:
                                variavel.confirmar_presenca()
                                self.ausentes.append(variavel)       
                   







                  
