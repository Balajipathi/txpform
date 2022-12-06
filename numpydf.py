


import streamlit as st
import numpy as np

# 10 rows 20 column
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)