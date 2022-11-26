import streamlit as st
st.write("""
# Graded Assignment 8
""")
#Get Input

st.header('User Input Parameters')

a = st.number_input("Enter value 1")
b = st.number_input("Enter value 2")

def multi(c,d):
    return c*d

st.subheader('Result')

st.write(multi(a,b))

