#coding:utf-8
from convocacao import Convocacao
from participante import Participante



class Reuniao:
      PREPARACAO = 1 
      CONFIRMADA = 2
      AGUARDANDO_APROVACAO_ATA = 3
      AGUARDANDO_ASSINATURA_ATA = 4
      CANCELADA = 5
      ATA_ASSINADA = 6
      contador = 0
      contador2 =0 
      def __init__(self,palta,data, hora ):
                 if palta != None:  
                      self.palta = palta
                      self.data = data
                      self.hora = hora
                      self.presentes = []
                      self.convocados = []
                      
                      self.estado = self.PREPARACAO

      
                 

      def cadastrar_local (self,local):

                 self.local = local    
      
      def alocar_pessoas(self,pessoa,data):
                 
                  convocado = Convocacao(pessoa,data, self)
                  #convocado.inserir(self)
                  self.convocados.append(convocado)
                  return self.convocados[self.contador]  
                  self.contador2 += 1
      def inserir_presentes(self,pessoa, data):

                 presente = Participante (pessoa, data)  
                 self.presentes.append(presente) 
                 return self.presentes[self.contador2] 
                 self.contador2 += 1
      def confirmar_reuniao (self):
                 if self.estado == 1:  
                      self.estado = self.CONFIRMADA 
                      

      def cadastrar_ata (self,ata):
                  self.ata = ata
                  self.estado = self.AGUARDANDO_APROVACAO_ATA  

      def cancelar_reuniao(self):
                  if self.estado <4 :
                       self.estado = self.CANCELADA  

      def aprovar_ata(self):
                  if self.estado == 3:
                       self.estado = self.AGUARDANDO_ASSINATURA_ATA                  
                       
   
      def assinatura_de_ata(self):

                   if self.estado == 4:
                       self.estado = self.ATA_ASSINADA 

      def desalocar_pessoa(self,pessoa):
                   for variavel in self.convocados:   
                        if variavel.pessoa == pessoa: 
                               variavel.desfazer_convocacao(None)
                               self.convocados.remove(variavel)  


      def retornar_estado(self):
                   return self.estado 
      def listar_ausentes(self):
                   self.ausentes = []  
                   for variavel in self.convocados:
                         variavel.confirmar() 
                         variavel.confirmar_presenca()
                         if variavel.estado == 5:
                             self.ausentes.append(variavel.pessoa)       
                   







                  
