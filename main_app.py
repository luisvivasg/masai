import streamlit as st
from datetime import datetime, timedelta

inicio_dias = datetime.now() - timedelta(730)
yesterday = datetime.now() - timedelta(2)
fecha_inicio_imp, first_date, fecha_inicio = datetime.strftime(inicio_dias, "%d-%B-%Y"), datetime.strftime(inicio_dias, "%Y %b %d"), datetime.strftime(inicio_dias, "%Y-%m-%d")
fecha_fin_imp, last_date, fecha_fin = datetime.strftime(yesterday, "%d-%B-%Y"), datetime.strftime(yesterday, "%Y %b %d"), datetime.strftime(yesterday, "%Y-%m-%d")
