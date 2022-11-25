import streamlit as st

st.write("""
# Graded Assignment 8 - Multiplication App
This app simply multiplies 2 numbers
""")

#Get Input
st.header('User Input Parameters')

num1 = st.number_input("Number 1")
num2 = st.number_input("Number 2")

def multiply(a,b):
	return float(a)*float(b)
n1=num1
n2=num2
result=multiply(n1,n2)
st.subheader('Result')
st.write('result')
