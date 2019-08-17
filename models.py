# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'
    def __init__ (self, nome, telefone, empresa):
        if(len(nome) < 3):
            raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
            
        self.nome       = nome
        self.telefone   = telefone
        self.empresa    = empresa
        self.__curtidas   = 0

    def imprimir(self):
        print "Nome : %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas
    
    @staticmethod
    def gerar_perfis(nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valor = linha.split(',')
            if(len(valor) is not 3 ):
                raise ArgumentoInvalidoError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
                
            perfis.append(Perfil(*valor))
        arquivo.close()
        return perfis
    
    
    
class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários Vip'
    def __init__ (self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido 

    def imprimir(self):
        print "Nome : %s, Telefone: %s, Empresa: %s, Apelido: %s" % (self.nome, self.telefone, self.empresa, self.apelido)
        
    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valor = linha.split(',')
            if(len(valor) is not 3 ):
                raise ArgumentoInvalidoError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
                
            perfis.append(classe(*valor))
        arquivo.close()
        return perfis
    
    
    
class ArgumentoInvalidoError(Exception):
    'Classe para tratamento de Exceptions'
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return repr(self.message)