import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1.6, 1.7) + [37.761221, -122.43221],
    columns=['lat', 'lon'])

st.map(df)
