# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 05:08:50 2021

@author: myla_
"""
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

py.init_notebook_mode(connected=True)

def grafico_atraso_viagem(arq2):
    
    quantidade_empresas = len(arq2) - 1
    empresas_percentual_atraso = []
    data = []
    
    while True:
        
        if quantidade_empresas>=0:
            
            empresa = arq2[quantidade_empresas]
            
            empresa["hora_realizada"] = pd.to_datetime(empresa["hora_realizada"], format='%Y-%m-%d %H:%M:%S')
            empresa["hora_realizada"] = empresa["hora_realizada"].dt.strftime('%H:%M:%S')
            empresa["hora_prevista"] = pd.to_datetime(empresa["hora_prevista"], format='%Y-%m-%d %H:%M:%S')
            empresa["hora_prevista"] = empresa["hora_prevista"].dt.strftime('%H:%M:%S')
            empresa['intervalo'] = np.where((empresa['hora_prevista']>'05:00:00') & (empresa['hora_prevista']<'08:00:00'), 1, 0)
            
            filtro = empresa['intervalo']==1
            empresa = empresa[filtro]
            
            empresa['duracao_realizada'] = empresa['duracao_realizada'].astype(float)
            empresa['duracao_prevista'] = empresa['duracao_prevista'].astype(float)
            empresa['atraso_viagem_percentual'] = np.where(empresa['duracao_realizada']>empresa['duracao_prevista'], 1, 0)
            agrupamento = empresa[['nome_linha', 'atraso_viagem_percentual']].groupby(['nome_linha']).mean()*100
            
            trace = go.Bar(x = agrupamento.index, 
                           y = agrupamento['atraso_viagem_percentual'],
                           name = empresa.iloc[0]['empresa'])
            data.append(trace)
            
            empresas_percentual_atraso.append(agrupamento)
            quantidade_empresas = quantidade_empresas - 1
            
        else:
            break
        
    layout = go.Layout(title = '<b>Gráfico de percentual de atraso em relação a duração de viagens de ônibus na cidade de Maceió no horário 05:00:00 até 08:00:00</b>',
                   xaxis = {'title': 'Nomes das linhas de ônibus'},
                   yaxis = {'title': 'Percentual de atraso na duração da viagem (%)'},
                   barmode = 'stack', template='plotly_white')
    
    fig = go.Figure(data=data, layout=layout)
    #py.plot(fig)
    py.iplot(fig)     
    return fig