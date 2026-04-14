import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Proiect Pachete Software",
    layout="wide"
)

st.title("Proiect Pachete Software")
st.subheader("Setup initial")

st.write("Aplicatia functioneaza.")

uploaded_file = st.file_uploader("Incarca CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Fisier incarcat")
    st.dataframe(df.head())

    st.write("Shape:")
    st.write(df.shape)
else:
    st.info("Incarca un fisier CSV")
