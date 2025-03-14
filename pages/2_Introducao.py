import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff



st.markdown('<h1 style="text-align: center;">Introdução do Dataset</h1>', unsafe_allow_html=True)
st.title("📊 Sobre o Conjunto de Dados")

st.write(
    "Este conjunto de dados contém **25.000 registros** de usuários da Netflix, "
    "gerados para análise, visualização e prática de machine learning. Ele inclui detalhes "
    "demográficos, tipo de assinatura, tempo de exibição e histórico de login de cada usuário."
)

st.subheader("📌 Colunas do Dataset")

st.write("- **User_ID** – Identificador único para cada usuário.")
st.write("- **Name** – Nome gerado aleatoriamente.")
st.write("- **Age** – Idade do usuário (entre 13 e 80 anos).")
st.write("- **Country** – País do usuário (escolhido aleatoriamente entre 10 opções).")
st.write("- **Subscription_Type** – Tipo de plano da Netflix (Basic, Standard, Premium).")
st.write("- **Watch_Time_Hours** – Total de horas assistidas no último mês.")
st.write("- **Favorite_Genre** – Gênero de conteúdo favorito do usuário.")
st.write("- **Last_Login** – Data do último login registrada no último ano.")

st.markdown('<h1 style="text-align: center;">Analise dos Dados da Netflix</h1>', unsafe_allow_html=True)

st.write("1 - Quais paises estão mais pré-dispostos a adquirir a assinatura premium?")
st.write("2 - Quais faixa etárias de usuarios estão dispostos a assinar o premium?")
st.write("3 - Que tipos de conteudo essa faixa etária prefere? ")
st.write("4 - Que tipo de contúdo ajudaria a captar mais usuários? ")


