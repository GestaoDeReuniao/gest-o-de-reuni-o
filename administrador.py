#coding:utf-8
from pessoa import Pessoa


class Administrador(Pessoa) :
    def __init__(self,senha):
        self.senha = senha
        
