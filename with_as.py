# -*- coding: UTF-8 -*-

#Para nao precisar utilizar o Try Except e Finally
#Pode usar o codigo abaixo e o Python cuida de tudo
#rodar no console c:\python with_as.py

with open('perfis.csv') as arquivo:
    for linha in arquivo:
        print linha
        
