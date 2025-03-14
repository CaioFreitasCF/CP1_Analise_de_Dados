import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Analise de Dados Serviços de Steaming", layout="wide")

st.markdown('<h1 style="text-align: center;">Sobre Mim</h1>', unsafe_allow_html=True)

st.write("""
Olá! Me chamo Caio, tenho 20 anos e sou estagiário em automação na T-Systems.
Trabalho com PHP para automação de processos e utilizo Laravel para o desenvolvimento de aplicações.
Atualmente, estou cursando Engenharia de Software na FIAP, onde aprimoro minhas habilidades e conhecimentos na área.
Meu objetivo é continuar evoluindo no campo da automação, criando soluções eficientes e inovadoras para otimizar processos.

Sempre busco aprender novas tecnologias e aprimorar minhas habilidades para me tornar um profissional cada vez mais qualificado.
""")
st.markdown('<h1 style="text-align: center; margin-bottom: 40px;">Meu Trabalho</h1>', unsafe_allow_html=True)

st.write("Em 2023 consegui meu estágio na empresa T-Systems e trabalho como estagiario de automação lidando com vários setores da empresa e automatizando processos , indo desde de bancos de dados a Power Automate")

st.image("imagens_logos/logo_t-systems.jpg", use_container_width=True)


st.markdown('<h1 style="text-align: center;">Minhas Certificações</h1>', unsafe_allow_html=True)

st.write("Em 2024 busquei evoluir em minha carreira profissional, junto aos cursos da AWS tirei minha primeira certificação:")

st.image("imagens_logos/CertificadoAWS.JPG", caption="Certificação AWS", use_container_width=True)

st.markdown('<h1 style="text-align: center; margin-bottom: 40px;">Linguagens</h1>', unsafe_allow_html=True)



col1, col2, col3 = st.columns(3)

# Adicionando imagens_logos nas colunas
with col1:
    st.image("imagens_logos/php_PNG18.png", use_container_width =True)

with col2:
    st.image("imagens_logos/png-clipart-laravel-black-logo-tech-companies.png", use_container_width =True)

with col3:
    st.image("imagens_logos/c.png", use_container_width =True)


col1, col2 = st.columns(2)

# Adicionando imagens_logos nas colunas
with col1:
    st.image("imagens_logos/github_PNG20.png", use_container_width =True)

with col2:
    st.image("imagens_logos/619137-middle.png", use_container_width =True)


st.markdown('<h1 style="text-align: center;">Instituições de Ensino</h1>', unsafe_allow_html=True)
st.write("Agora em 2025 continuo meus estudos no curso de Engenharia de Software da Fiap e, faço os cursos de programação da Alura para complementar meus conhecimentos e sempre buscar evoluir minha carreira ")



col1, col2 = st.columns(2)

# Adicionando imagens_logos nas colunas
with col1:
    st.image("imagens_logos/fiap.png", use_container_width =True)

with col2:
    st.image("imagens_logos/alura.png", use_container_width =True)


