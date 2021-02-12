# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:17:03 2021

@author: myla_
"""

import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

py.init_notebook_mode(connected=True)


def grafico_atraso_linha(df):#função para geração de gráfico de atraso de viagem em relação a linha de ônibus
    
    df["hora_realizada"] = pd.to_datetime(df["hora_realizada"], format='%Y-%m-%d %H:%M:%S')
    df["hora_prevista"] = pd.to_datetime(df["hora_prevista"], format='%Y-%m-%d %H:%M:%S')
    df['percentual_atraso_saida'] = np.where(df['hora_prevista']<df['hora_realizada'], 1, 0)
    
    agrupamento = df[['nome_linha', 'percentual_atraso_saida']].groupby(['nome_linha']).mean()*100
    
    trace = go.Bar(x = agrupamento.index,
               y = agrupamento['percentual_atraso_saida'],
               marker = {'color': '#ff9f43'})
    data = [trace]
    
    layout = go.Layout(title = '<b>Gráfico de percentual de atraso de viagens de ônibus na cidade de Maceió</b>',
                   xaxis = {'title': 'Nomes das linhas de ônibus'},
                   yaxis = {'title': 'Percentual de atraso na saída (%)'},
                   barmode = 'stack', template='plotly_white')
    
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)
    
    return agrupamento


def grafico_atraso_empresa(df):#função para geração de gráfico de atraso de viagem em relação a empresa
    
    df["hora_realizada"] = pd.to_datetime(df["hora_realizada"], format='%Y-%m-%d %H:%M:%S')
    df["hora_prevista"] = pd.to_datetime(df["hora_prevista"], format='%Y-%m-%d %H:%M:%S')
    df['percentual_atraso_saida'] = np.where(df['hora_prevista']<df['hora_realizada'], 1, 0)
    
    agrupamento = df[['empresa', 'percentual_atraso_saida']].groupby(['empresa']).mean()*100
    
    trace = go.Bar(x = agrupamento.index,
               y = agrupamento['percentual_atraso_saida'],
               marker = {'color': '#ff9f43'})
    data = [trace]
    
    layout = go.Layout(title = '<b>Gráfico de percentual de atraso de viagens de ônibus na cidade de Maceió</b>',
                   xaxis = {'title': 'Empresas de linhas de ônibus'},
                   yaxis = {'title': 'Percentual de atraso na saída (%)'},
                   barmode = 'stack', template='plotly_white')
    
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)
    
    return agrupamento


def grafico_atraso_sentido(df):#função para geração de gráfico de atraso de viagem em relação ao sentido
    
    df["hora_realizada"] = pd.to_datetime(df["hora_realizada"], format='%Y-%m-%d %H:%M:%S')
    df["hora_prevista"] = pd.to_datetime(df["hora_prevista"], format='%Y-%m-%d %H:%M:%S')
    df['percentual_atraso_saida'] = np.where(df['hora_prevista']<df['hora_realizada'], 1, 0)
    
    agrupamento = df[['sentido_viagem', 'percentual_atraso_saida']].groupby(['sentido_viagem']).mean()*100
    
    trace = go.Bar(x = agrupamento.index,
               y = agrupamento['percentual_atraso_saida'],
               marker = {'color': '#ff9f43'})
    data = [trace]
    
    layout = go.Layout(title = '<b>Gráfico de percentual de atraso de viagens de ônibus na cidade de Maceió</b>',
                   xaxis = {'title': 'Sentido das viagens'},
                   yaxis = {'title': 'Percentual de atraso na saída (%)'},
                   barmode = 'stack', template='plotly_white')
    
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)
    
    return agrupamento