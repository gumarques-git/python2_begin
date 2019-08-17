# -*- coding: UTF-8 -*-

print('Chamar metodo teste_erro + nome_arquivo')

def teste_erro(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        print('arquivo aberto')
        arquivo.close()
    except IOError as erro:
        print('Deu IOError: %s' % nome_arquivo)

        
