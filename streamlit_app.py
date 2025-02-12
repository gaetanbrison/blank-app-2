## Import packages

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## 

st.title("Welcome to DS")

st.image("cat.jpg")

app_mode = st.sidebar.selectbox("Click on the page:",["01 Introduction","02 Data Viz"])

df = pd.read_csv("wine.csv")

if app_mode == "01 Introduction":
    st.write("Let's start exploring the dataset")

    st.dataframe(df.head(5))

    st.dataframe(df.describe())


if app_mode == "02 Data Viz":
    st.write("Let's visualize data")

    list_of_variables = df.columns
    user_selection = st.selectbox("Select a variable",list_of_variables)
    st.bar_chart(df[user_selection])


    user_selections = st.multiselect("Select a variable",list_of_variables)

    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=user_selections[0],y=user_selections[1], data=df)
    st.pyplot(fig)


