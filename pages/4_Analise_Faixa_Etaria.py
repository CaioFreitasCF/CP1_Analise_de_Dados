import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "netflix_users.xlsx"
df = pd.read_excel(file_path)

# Filtrar apenas assinantes Premium
df_premium = df[df["Subscription_Type"].str.lower() == "premium"]

# Cálculo das medidas centrais
idade_media = df_premium["Age"].mean()
idade_mediana = df_premium["Age"].median()
idade_moda = df_premium["Age"].mode()[0]

genero_moda = df_premium["Favorite_Genre"].mode()[0]

tempo_medio = df_premium["Watch_Time_Hours"].mean()
tempo_mediano = df_premium["Watch_Time_Hours"].median()

# Criar faixas etárias
bins = [10, 20, 30, 40, 50, 60, 70, 80]
labels = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]

# ✅ Corrigindo SettingWithCopyWarning
df_premium.loc[:, "Faixa_Etaria"] = pd.cut(df_premium["Age"], bins=bins, labels=labels, right=False)

# Calcular média de horas assistidas por faixa etária
faixa_etaria_watch = df_premium.groupby("Faixa_Etaria", observed=False)["Watch_Time_Hours"].mean().reset_index()

# Criar página no Streamlit
st.title("📊 Análise de Assinantes Premium da Netflix")

# Idade dos Assinantes Premium
st.header("1️⃣ Qual faixa etária mais assina o plano Premium?")
st.subheader("Idade dos Assinantes Premium")
st.write(f"- **Média**: {idade_media:.2f} anos")
st.write(f"- **Mediana**: {idade_mediana:.2f} anos")
st.write(f"- **Moda**: {idade_moda} anos")

# Gráfico de distribuição da idade
fig, ax = plt.subplots()
sns.histplot(df_premium["Age"], bins=20, kde=True, ax=ax)
ax.set_title("Distribuição da Idade dos Assinantes Premium")
ax.set_xlabel("Idade")
ax.set_ylabel("Quantidade")
st.pyplot(fig)

st.write("Os dados indicam que a faixa etária de 40 a 49 anos é a que mais assina o plano Premium.")

# Gênero Favorito dos Assinantes Premium
st.subheader("Gênero Favorito dos Assinantes Premium")
st.write(f"- **Moda**: {genero_moda}")

# Gráfico de barras do gênero favorito
fig, ax = plt.subplots()
sns.countplot(y=df_premium["Favorite_Genre"], order=df_premium["Favorite_Genre"].value_counts().index, ax=ax)
ax.set_title("Gênero Favorito dos Assinantes Premium")
ax.set_ylabel("Gêneros Favoritos")
ax.set_xlabel("Quantidade de Espectadores")
st.pyplot(fig)

st.write("O gênero favorito dos assinantes Premium é 'Horror'. Para manter esse público engajado, a Netflix deve considerar expandir seu catálogo nesse gênero.")

# Tempo de Assistência dos Assinantes Premium
st.subheader("Tempo de Assistência dos Assinantes Premium")
st.write(f"- **Média**: {tempo_medio:.2f} horas")
st.write(f"- **Mediana**: {tempo_mediano:.2f} horas")

# Gráfico de distribuição do tempo assistido
fig, ax = plt.subplots()
sns.histplot(df_premium["Watch_Time_Hours"], bins=20, kde=True, ax=ax)
ax.set_title("Distribuição do Tempo Assistido pelos Assinantes Premium")
ax.set_xlabel("Tempo assistido (horas)")
ax.set_ylabel("Quantidade")
st.pyplot(fig)

st.write(
    "O gráfico mostra que a maioria dos usuários Premium não assiste à plataforma por longos períodos de tempo. "
    "Para aumentar o engajamento, é essencial analisar os usuários que mais consomem conteúdo e entender suas preferências."
)

# --- Analisando usuários fora do plano Premium ---

# Filtrar usuários fora do plano Premium
df_non_premium = df[df["Subscription_Type"].str.lower() != "premium"]

# ✅ Corrigindo SettingWithCopyWarning
df_non_premium.loc[:, "Faixa_Etaria"] = pd.cut(df_non_premium["Age"], bins=bins, labels=labels, right=False)

# ✅ Corrigindo FutureWarning de observed=False
faixa_etaria_watch_non_premium = df_non_premium.groupby("Faixa_Etaria", observed=False)["Watch_Time_Hours"].mean().reset_index()

# Encontrar a faixa etária com maior média de horas assistidas
faixa_etaria_mais_assiste = faixa_etaria_watch_non_premium.loc[faixa_etaria_watch_non_premium["Watch_Time_Hours"].idxmax()]

# Encontrar o gênero mais popular dessa faixa etária
faixa_etaria_mais_assiste_users = df_non_premium[df_non_premium["Faixa_Etaria"] == faixa_etaria_mais_assiste["Faixa_Etaria"]]
genero_mais_popular = faixa_etaria_mais_assiste_users["Favorite_Genre"].mode()[0]

# Gráfico de linha do tempo assistido por faixa etária fora do plano Premium
fig, ax = plt.subplots()
sns.lineplot(
    x=faixa_etaria_watch_non_premium["Faixa_Etaria"],
    y=faixa_etaria_watch_non_premium["Watch_Time_Hours"],
    marker="o",
    color="blue",
    linewidth=2
)
ax.set_title("Média de Tempo Assistido por Faixa Etária (Fora do Plano Premium)")
ax.set_xlabel("Faixa Etária")
ax.set_ylabel("Média de Horas Assistidas")
ax.grid(True, linestyle="--", alpha=0.5)  # Adiciona linhas de grade leves para melhor visualização
st.pyplot(fig)

# Exibir a faixa etária que mais assiste e o gênero favorito
st.subheader("📊 Faixa Etária Fora do Plano Premium que Mais Assiste")
st.write(f"- **Faixa Etária**: {faixa_etaria_mais_assiste['Faixa_Etaria']}")
st.write(f"- **Média de Horas Assistidas**: {faixa_etaria_mais_assiste['Watch_Time_Hours']:.2f} horas")
st.write(f"- **Gênero Favorito**: {genero_mais_popular}")

# Recomendação para a Netflix
st.subheader("💡 Conclusão")
st.write("""A análise dos assinantes Premium da Netflix revelou que a faixa etária predominante no plano Premium é de 40 a 49 anos, enquanto o gênero de conteúdo mais consumido por esse público é Horror. Além disso, observamos que, apesar de serem assinantes, muitos usuários não passam longos períodos assistindo à plataforma.

Por outro lado, entre os usuários que ainda não assinam o plano Premium, aqueles que mais assistem à Netflix estão concentrados em uma faixa etária diferente, com um grande interesse por documentários. Esse comportamento sugere uma oportunidade para a empresa expandir sua base de assinantes Premium ao investir mais nesse tipo de conteúdo.

Diante dessas descobertas, recomendamos que a Netflix aumente a oferta de documentários, visando converter esse público mais engajado em assinantes Premium. Além disso, uma possível redução no preço do plano poderia atrair ainda mais clientes fiéis, aumentando a retenção e a estabilidade da receita. Paralelamente, manter o investimento no gênero Horror garantirá que os atuais assinantes Premium continuem satisfeitos e consumindo mais horas de conteúdo, fortalecendo ainda mais o modelo de negócios da empresa.

Dessa forma, ao alinhar sua estratégia de conteúdo e preços com o comportamento dos usuários, a Netflix pode não apenas atrair novos assinantes, mas também aumentar o tempo de permanência na plataforma e a fidelização do público Premium. 🚀""")
