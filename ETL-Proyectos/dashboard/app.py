import streamlit as st
import duckdb
import pandas as pd

st.title(" Crypto Market Dashboard")

con = duckdb.connect("data/warehouse.duckdb")
df = con.execute("SELECT * FROM crypto_prices").df()

st.metric("Total monedas", len(df))
st.metric("Mayor cap", df.loc[df.market_cap.idxmax(), "name"])

st.bar_chart(df.set_index("name")["market_cap"].head(10))
st.dataframe(df)