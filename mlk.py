import streamlit as st
st.title("Webcome to Yash website")
st.header("Bsc computer science 3 year")
st.subheader("A Gift For You")
name=st.text_input("Write your name : ")
button=st.button("OK")
if button :
    st.markdown(f""":{name}""")
