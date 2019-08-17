# -*- coding: UTF-8 -*-


from models import *

arquivo = None #inicializando variavel para usar no If
nome_arquivo = 'perfis.csv'
try:
    arquivo = open(nome_arquivo, 'r')
    valores = arquivo.readline().split(',') #usamos dois ponto ':' para simular erro
    perfil = Perfil(*valores)
except (IOError, TypeError) as erro:
    print('Deu Exception: %s' % erro)
finally:
    if(arquivo is not None):
        print('Fechando o arquivo: %s' % nome_arquivo)
        arquivo.close()

        
