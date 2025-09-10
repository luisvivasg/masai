import streamlit as st
from datetime import datetime, timedelta
from funciones import conteo_etnias
import plotly.graph_objects as go

st.write("**Ethnicity relevance in MEdia**")
inicio_dias = datetime(2017, 1, 1)

etnia = {"Maasai":"Kenya", "Zulu":"Africa", "Igbo":"Nigeria"}
etnia_s = st.selectbox("Select Ethnicity", etnia)

if st.button("Get data and chart"):
    yesterday = datetime.now() - timedelta(2)
    fecha_inicio_imp, first_date, fecha_inicio = datetime.strftime(inicio_dias, "%d-%B-%Y"), datetime.strftime(inicio_dias, "%Y %b %d"), datetime.strftime(inicio_dias, "%Y-%m-%d")
    fecha_fin_imp, last_date, fecha_fin = datetime.strftime(yesterday, "%d-%B-%Y"), datetime.strftime(yesterday, "%Y %b %d"), datetime.strftime(yesterday, "%Y-%m-%d")

    st.write(f"**Ethnicity relevance for {etnia_s} ({fecha_inicio_imp} to {fecha_fin_imp})**")
    df_etnia = conteo_etnias(etnia_s, etnia[etnia_s], fecha_inicio, fecha_fin)
    st.write(df_etnia)
    df_etnia["datetime"] = df_etnia["datetime"].dt.tz_localize(None)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_etnia["datetime"],
        y=df_etnia["Article Count"],
        mode="lines",
        name="Ethnicity count",

    ))
    st.plotly_chart(fig)



