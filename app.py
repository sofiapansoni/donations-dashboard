#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:16:51 2024

@author: sofiapansoni
"""
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline

# Caricamento dei dati
data = pd.read_excel('/Users/sofiapansoni/Desktop/Progetto LFO/Campagne 2023/marketing mix model- prime analisi  con data 23-24.xlsx')

# Preparazione dei dati
features = ['SPEND META', 'SPEND TV', 'SPEND ADS']
target = 'DONATIONS TOTAL'
X = data[features]
y = data[target]

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modello di regressione Ridge con standardizzazione
ridge_model = make_pipeline(StandardScaler(), Ridge())
ridge_model.fit(X_train, y_train)
y_pred_ridge = ridge_model.predict(X_test)

mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

# Funzione per fare previsioni
def predici_donazioni(spend_meta, spend_tv, spend_ads):
    new_data = {
        'SPEND META': [spend_meta],
        'SPEND TV': [spend_tv],
        'SPEND ADS': [spend_ads]
    }
    new_data_df = pd.DataFrame(new_data)
    pred = ridge_model.predict(new_data_df)
    return pred

# Interfaccia Streamlit
st.title('Dashboard Predizione Donazioni')

st.sidebar.header('Input Nuovi Investimenti')
spend_meta = st.sidebar.number_input('Investimento in Meta', min_value=0.0, step=100.0)
spend_tv = st.sidebar.number_input('Investimento in TV', min_value=0.0, step=100.0)
spend_ads = st.sidebar.number_input('Investimento in ADS', min_value=0.0, step=100.0)

if st.sidebar.button('Predici Donazioni'):
    predizione = predici_donazioni(spend_meta, spend_tv, spend_ads)
    st.write(f'Predizione del numero di donazioni: {predizione[0]:.2f}')

st.header('Dati Storici')
st.write(data)

st.header('Valutazione del Modello')
st.write(f'MSE (Ridge Regression): {mse_ridge:.2f}')
st.write(f'R^2 (Ridge Regression): {r2_ridge:.2f}')

