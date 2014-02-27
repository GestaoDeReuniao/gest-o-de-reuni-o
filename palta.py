#coding:utf-8




class Palta:

      def __init__ (self, titulo, questao=[]):
          self.titulo = titulo
          self.questao = questao       

      def inserir_questao(self, questao):
          self.questao.append(questao)
