import streamlit as st
import pandas as pd

# Upload CSV
file = st.file_uploader("Upload your CSV file")
if file is not None:
    df = pd.read_csv(file, encoding="latin1")
    st.write("📄 Data Preview:", df.head())

    # ตัวอย่างกราฟ
    st.line_chart(df["Ship Mode"])