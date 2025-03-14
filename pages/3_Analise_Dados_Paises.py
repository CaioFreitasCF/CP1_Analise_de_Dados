import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import altair as alt

st.title("Quais paises estão mais pré-dispostos a adquirir a assinatura premium?")
st.write("Média de assinantes premium por pais : ")

# Nome do arquivo (ele deve estar na mesma pasta do script)
# Nome do arquivo (ele deve estar na mesma pasta do script)
file_path = "netflix_users.xlsx"  # Substitua pelo nome correto do arquivo

# Nome do arquivo (ele deve estar na mesma pasta do script)
file_path = "netflix_users.xlsx"  # Substitua pelo nome correto do arquivo

# Título do app
st.title("🏆 Ranking de Assinantes da Netflix por País")

try:
    # Lê o arquivo Excel
    df = pd.read_excel(file_path)

    # Verifica se as colunas esperadas estão no arquivo
    expected_columns = {"Country", "Subscription_Type", "Watch_Time_Hours"}
    if not expected_columns.issubset(df.columns):
        st.error(f"O arquivo deve conter as colunas: {expected_columns}")
    else:
        # 📌 Ranking de países com mais assinantes Premium
        st.subheader("📊 Ranking dos países com mais assinantes Premium")
        st.write("Os dados abaixo indicam que Alemanha, Brasil e EUA são os países que mais assinam o Premium da Netflix.")
        st.write("Mas existe um modo de aumentar o número de assinantes Premium em outros países:")

        df_premium = df[df["Subscription_Type"].str.lower() == "premium"]
        ranking_premium = df_premium["Country"].value_counts().reset_index()
        ranking_premium.columns = ["Country", "Subscribers"]
        ranking_premium = ranking_premium.sort_values(by="Subscribers", ascending=False)
        ranking_premium.insert(0, "Rank", range(1, len(ranking_premium) + 1))

        st.dataframe(ranking_premium)

        chart_premium = alt.Chart(ranking_premium).mark_bar(color="steelblue").encode(
            x=alt.X("Country:N", sort="-y", title="País"),
            y=alt.Y("Subscribers:Q", title="Número de Assinantes"),
        ) + alt.Chart(ranking_premium).mark_line(color="red", point=True).encode(
            x="Country:N",
            y="Subscribers:Q",
        )

        st.altair_chart(chart_premium, use_container_width=True)

        # 📌 Ranking de países com mais assinantes Basic
        st.subheader("📊 Ranking dos países com mais assinantes Basic")
        st.write("Aqui podemos ver quais países preferem a assinatura Basic e como podemos incentivar upgrades para planos superiores.")

        df_basic = df[df["Subscription_Type"].str.lower() == "basic"]
        ranking_basic = df_basic["Country"].value_counts().reset_index()
        ranking_basic.columns = ["Country", "Subscribers"]
        ranking_basic = ranking_basic.sort_values(by="Subscribers", ascending=False)
        ranking_basic.insert(0, "Rank", range(1, len(ranking_basic) + 1))

        st.dataframe(ranking_basic)

        chart_basic = alt.Chart(ranking_basic).mark_bar(color="green").encode(
            x=alt.X("Country:N", sort="-y", title="País"),
            y=alt.Y("Subscribers:Q", title="Número de Assinantes"),
        ) + alt.Chart(ranking_basic).mark_line(color="red", point=True).encode(
            x="Country:N",
            y="Subscribers:Q",
        )

        st.altair_chart(chart_basic, use_container_width=True)

        # 📌 Ranking de países que mais assistem Netflix (Watch_Time_Hours)
        st.subheader("⏳ Ranking dos países que mais assistem à Netflix (horas)")
        st.write("Este ranking mostra quais países têm maior engajamento na plataforma em termos de horas assistidas.")
        st.write("Com isso podemos ver que vários paises que são muito engajados não estão assinando o premium.")
        st.write("Mas por que? Uma das possibilidades é o tipo de conteudo da plataforma e seu público alvo")
        ranking_tempo = df.groupby("Country")["Watch_Time_Hours"].sum().reset_index()
        ranking_tempo = ranking_tempo.sort_values(by="Watch_Time_Hours", ascending=False)
        ranking_tempo.insert(0, "Rank", range(1, len(ranking_tempo) + 1))

        st.dataframe(ranking_tempo)

        chart_tempo = alt.Chart(ranking_tempo).mark_bar(color="purple").encode(
            x=alt.X("Country:N", sort="-y", title="País"),
            y=alt.Y("Watch_Time_Hours:Q", title="Horas Assistidas"),
        ) + alt.Chart(ranking_tempo).mark_line(color="orange", point=True).encode(
            x="Country:N",
            y="Watch_Time_Hours:Q",
        )

        st.altair_chart(chart_tempo, use_container_width=True)

except FileNotFoundError:
    st.error(f"❌ O arquivo '{file_path}' não foi encontrado na pasta do projeto.")

