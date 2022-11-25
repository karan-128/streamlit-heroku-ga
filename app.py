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
	
values = {
	'num1': num1,
	'num2': num2
}
	
data = pd.DataFrame(values, index=[0])
return data
st.subheader('User Input parameters')
st.write(df.to_dict())

def multiply(a,b):
	return float(a)*float(b)

st.write(multiply(num1,num2))
