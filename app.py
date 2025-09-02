import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("data.csv")

# Título
st.title("📊 Dashboard de Educação")

# Filtros
anos = st.multiselect("Selecione o(s) ano(s):", df["Ano"].unique(), default=df["Ano"].unique())
regioes = st.multiselect("Selecione a(s) região(ões):", df["Região"].unique(), default=df["Região"].unique())

df_filtrado = df[(df["Ano"].isin(anos)) & (df["Região"].isin(regioes))]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total de Alunos", df_filtrado["Alunos"].sum())
col2.metric("Total de Escolas", df_filtrado["Escolas"].sum())
col3.metric("Média de Alunos/Escola", round(df_filtrado["Alunos"].sum() / df_filtrado["Escolas"].sum(), 2))

# Gráfico 1 - Alunos por Ano
fig1 = px.bar(df_filtrado, x="Ano", y="Alunos", color="Região", barmode="group", title="Alunos por Ano e Região")
st.plotly_chart(fig1)

# Gráfico 2 - Distribuição por Sexo
fig2 = px.pie(df_filtrado, names="Sexo", values="Alunos", title="Distribuição por Sexo")
st.plotly_chart(fig2)

# Gráfico 3 - Evolução no Tempo
fig3 = px.line(df_filtrado, x="Ano", y="Alunos", color="Região", markers=True, title="Evolução de Alunos")
st.plotly_chart(fig3)

# Tabela
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado)
