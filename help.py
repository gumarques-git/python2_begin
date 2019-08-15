# -*- coding: UTF-8 -*-

import math

class Data(object):
    'Classe auxiliar para Datas'
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprimir(self):
#       print self.dia +'/'+ self.mes +'/'+ self.ano
        print '%s/%s/%s' % (self.dia, self.mes, self.ano)


class Pessoa(object):
    'Classe para calcular IMC'
    def __init__(self, nome, peso, altura):
        self.nome   = nome
        self.peso   = peso
        self.altura = altura
        self.IMC    = peso / math.pow(altura, 2)

    def imprimir(self):
        print "IMC de: %s : %s." % (self.nome, self.IMC)