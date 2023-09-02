import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1, 2) + float([37.761221, -122.43221]),
    columns=['lat', 'lon'])

st.map(df)
