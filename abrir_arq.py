# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:13:16 2021

@author: myla_
"""

import pandas as pd


def abrir_arquivo(arquivo):#função responsável por abrir o arquivo no formato csv
    
    df = pd.read_csv(arquivo, sep = ',', header = 0, encoding='UTF-8', 
                     index_col = 0, decimal=b',')

    return df