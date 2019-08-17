# -*- coding: UTF-8 -*-


from models import *

arquivo = None #inicializando variavel para usar no If
nome_arquivo = 'perfis.csv'
try:
    arquivo = open(nome_arquivo, 'r')
    valores = arquivo.readline().split(',') #usamos dois ponto ':' para simular erro
    perfil = Perfil(*valores)
finally:
    if(arquivo is not None):
        print('Fechando o arquivo: %s' % nome_arquivo)
        arquivo.close()

        
