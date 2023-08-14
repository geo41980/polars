import pandas as pd
import pygwalker as pyg
import streamlit as st


st.set_page_config(layout="wide")


st.title("Data Analysis with PyGWalker.")

df = None


with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file")
    if uploaded_files is not None:
        df = pd.read_csv(uploaded_files)


if df is not None:
    df = df.reset_index()
    html_output = pyg.walk(df, env='Streamlit')
    st.write(html_output, unsafe_allow_html=True)
    #st.markdown(html_output, unsafe_allow_html=True)
else:
    st.write("No se ha cargado ningún archivo CSV.")
