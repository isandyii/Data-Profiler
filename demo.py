import pandas as pd
import streamlit as st

df=pd.read_csv(r"D:\DS Course\Pandas work\DataFiles\demo_dataset.csv")

st.dataframe(df.describe(include="all").astype("str"))