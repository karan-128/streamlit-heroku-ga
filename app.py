import streamlit as st
import pandas as pd
st.write("""
# Graded Assignment 8 - Multiplication App
This app simply multiplies 2 numbers
""")
#Get Input
st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("Number 1")
    num2 = st.number_input("Number 2")
df = user_input_features()	

st.subheader('User Input parameters')

def multiply(a,b):
	return float(a)*float(b)

st.write(multiply(df['num1'],df['num2']))
