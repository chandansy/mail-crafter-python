import streamlit as st
import streamlit_authenticator as stauth




# Sign up section

def sign_up():
    with st.form(key='signup'):
        st.header('Sign up')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        confirm_password = st.text_input('Confirm password', type='password')
        submit_button = st.form_submit_button(label='Sign up')



sign_up()