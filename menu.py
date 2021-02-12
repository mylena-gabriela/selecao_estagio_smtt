# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:14:20 2021

@author: myla_
"""

from abrir_arq import abrir_arquivo
from grafico_percentual_atraso import (grafico_atraso_linha, 
                                       grafico_atraso_empresa, 
                                       grafico_atraso_sentido)


arquivo = "viagens.csv"
df = abrir_arquivo(arquivo)

grafico1 = grafico_atraso_linha(df)
#grafico2 = grafico_atraso_empresa(df)
#grafico3 = grafico_atraso_sentido(df)