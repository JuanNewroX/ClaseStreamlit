import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime

@st.cache
def dowload_data():
    data_source = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
    return (pd.read_csv(data_source).rename(columns={'Lat':'lat', 'Lon':'lon'}))

data = dowload_data()

format = 'HH:MM'
start_date = datetime.time(00,00)
end_date = datetime.time(23,59)

data["Date/Time"] = pd.to_datetime(data["Date/Time"], format='%m/%d/%Y %H:%M:%S')
data['HourOfDay'] = data['Date/Time'].dt.time

time_slider = st.sidebar.slider('Seleccione las horas',
                               start_date,
                               end_date,
                               (start_date, end_date),
                               format=format)

st.sidebar.write("Hora inicio:", time_slider[0])
st.sidebar.write("Hora fin:", time_slider[1])

st.title("UBER PICKUPS DATA")
st.subheader("Resumen de datos")
df = data[(data.HourOfDay > time_slider[0]) & (data.HourOfDay < time_slider[1])]

cantidad_x_page = 1000
if len(df) < 1000:
    cantidad_x_page = len(df)

slider = st.sidebar.slider("Seleccione la pagina", 1, int(len(df)/cantidad_x_page))
st.sidebar.write("Cantidad x pagina:", cantidad_x_page)
st.sidebar.write("Cantidad de paginas:", int(len(df)/cantidad_x_page) )

df = df.loc[(slider - 1) * cantidad_x_page:(slider) * cantidad_x_page]
df.loc[:, df.columns != 'HourOfDay']

st.subheader("Mapa de datos")
st.map(df)

#st.write(df.groupby([pd.Grouper(key='HourOfDay',freq='H'),df.Base]).size().reset_index(name='count'))

st.line_chart(data.groupby(data['Date/Time'].dt.hour).size().reset_index(name='count'))
st.bar_chart(data.groupby(data['Date/Time'].dt.hour).size().reset_index(name='count'))