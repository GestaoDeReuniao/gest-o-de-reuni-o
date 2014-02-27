#coding:utf-8



class  Questao :
      
       def __init__(self,titulo,ponto =[]):
              self.ponto = ponto 
              self.titulo = titulo
       def inserir_ponto(self, ponto):
              self.ponto.append(ponto)
