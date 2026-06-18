import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv(

        "bank_transactions.csv",

        low_memory=False

    )

    return df