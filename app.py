import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Análise de Anúncios de Venda de Carros')
st.dataframe(df.head())

st.subheader('Distribuição de Preços')
if st.checkbox('Mostrar histograma de preços'):
    fig = px.histogram(df, x='price', title='Distribuição de Preços dos Veículos')
    st.plotly_chart(fig)

st.subheader('Preço vs Odômetro')
if st.checkbox('Mostrar gráfico de dispersão'):
    fig = px.scatter(
        df, x='odometer', y='price',
        title='Preço vs Odômetro',
        labels={'odometer': 'Quilometragem', 'price': 'Preço'}
    )
    st.plotly_chart(fig)