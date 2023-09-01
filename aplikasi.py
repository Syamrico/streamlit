import streamlit as st
import pandas as pd
import numpy as np
# from prediction import predict

st.title('Tebak ini Bunga apa ??')
st.markdown('Toy model untuk bermain tebak bunga
            setosa, versicolor, virginica')

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
  st.text("Karakter bentuk kelopak yang diamati")
  sepal_l = st.slider('Panjang Kelopak (cm)', 1.0, 8.0, 0.5)
  sepal_w = st.slider('Lebar Kelopak (cm)', 2.0, 4.4, 0.5)

with col2:
  st.text("Karakter bentuk mahkota yang diamati")
  petal_l = st.slider('Panjang Mahkota (cm)', 1.0, 7.0, 0.5)
  petal_w = st.slider('Lebar Mahkota (cm)', 0.1, 2.5, 0.5)

st.button("Prediksi tipe Bunga")
