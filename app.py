import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import Data

data = pd.read_csv('.\owid-covid-data.csv')

mex_data = data[data['location'] == 'Mexico']

total_deaths = mex_data['total_deaths'].max()

st.write("Tabla de datos de COVID-19 en Mexico:")
st.write(mex_data)
st.write(f"Total de muertes por COVID-19 en Mexico: {total_deaths}")