import streamlit as st

st.set_page_config(page_title="My First Website",page_icon="🟢",layout="centered")
st.title("Welcome To My First Python Website.")

st.sidebar.title("Navigation")
page= st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home Page")
    st.write("This is a simple homepage built python and Streamlit")
    name = st.text_input("Whats\s your name?")
    if name:
        st.success(f'Hello {name}! Thanks for visitig.')
elif page == "About":
    st.header("About")
    st.write("This website is built entirly using python and Streamlit in under 15 minutes!")
    
elif page == "Contact":
    st.header("Contact US")
    email = st.text_input("Your email")
    message = st.text_input("Your message")
    if st.button("Submit"):
        st.success("Thank you. We have received your message.")