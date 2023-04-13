import streamlit as st

st.write("Hello")
st.write("Hello")

st.header("st.button")
if st.button("say hi"):
    st.write("hi")
else:
    st.write("bye")
    
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
