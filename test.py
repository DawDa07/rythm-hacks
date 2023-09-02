import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1, 2) / [50, 50] + [37.7612, -122.432],
    columns=['lat', 'lon'])

st.map(df)
