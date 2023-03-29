import pandas as pd
import streamlit as st

@st.cache_data
def get_place(n=''):
    return pd.read_csv('data/place.csv').sample(frac=1)