# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 05:11:44 2021

@author: myla_
"""

def divisao_empresas(df):
    
    linhas = df['empresa'].copy()
    linhas = linhas.drop_duplicates().reset_index().drop('index', axis=1).empresa
    
    x = 0
    z = len(linhas)
    empresas_onibus = []
    
    while True:
        if x<z:
            df_mask = df['empresa'] == linhas[x]
            filtered_df = df[df_mask]
            empresas_onibus.append(filtered_df)
            x = x + 1
        else:
            break
    
    return empresas_onibus