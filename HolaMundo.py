import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Hola mundo")
x = 4
st.write(x, "El resultado es ", x*x)

st.write("Now using dataframe")
df = pd.DataFrame({
    "Columna A": [1,2,3,4,5,6],
    "Columna C": ['A', 'B', 'C', 'C', 'A', '2']
})
st.write(df)

chart_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A','B', 'C']
)
st.line_chart(chart_df)
map = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.79, -122.4],
    columns=['lat', 'lon']
)


if st.checkbox("Show me"):
    st.map(map)

x = st.slider("Select")

opcion = st.selectbox(
    "Select",
    [1,2,3,4,5,6,7,8,9,10]
)
progressbar = st.progress(0)
progressbar2 = st.progress(0)
progres_e = st.empty()
for i in range(100):
    progressbar.progress(i)
    time.sleep(0.1)
    progressbar2.progress(i)
    progres_e.text(i)

options_side = st.sidebar.selectbox("Seleccione", ["1", "2", "3"])

anotherslides = st.sidebar.slider("Slide 2 ", 0, 100, (25, 100))


