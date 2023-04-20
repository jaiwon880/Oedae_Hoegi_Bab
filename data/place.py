import pandas as pd
import streamlit as st

@st.cache_data
def get_place(n=''):
    return pd.read_csv('data/oedae_place.csv').sample(frac=1)
    # , pd.read_csv('data/hoegi_place.csv').sample(frac=1)