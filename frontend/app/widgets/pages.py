from time import sleep
import streamlit as st
import pandas as pd
from service.api_functions import Formula1Data, Auth

class Pages:
    @staticmethod
    def main_page():
        drivers_json = Formula1Data.get_driver_data()
        drivers_df = pd.DataFrame(drivers_json["data"], columns=drivers_json["columns"])
        st.dataframe(drivers_df)
    
    @staticmethod
    def public_page():
        st.header('F1 Database')

        c1,c2 = st.columns(2)
        with c1: 
            if st.button('Login',use_container_width=True): 
                st.session_state.current_page = 'login_page'
                st.experimental_rerun()
        
        with c2:
            if st.button('Register',use_container_width=True): 
                st.session_state.current_page = 'register_page'
                st.experimental_rerun()


    
    @staticmethod
    def login_page():
        st.header('Login')
        with st.form('Login'):
            c1, c2 = st.columns(2)
            with c1: user = st.text_input('Username')
            with c2: password = st.text_input('Password',type='password')
            if st.form_submit_button('Login',use_container_width=True):
                if Auth.get_token(user,password):
                    st.session_state.current_page = 'home_page'
                    st.experimental_rerun()
        if st.button('Register',use_container_width=True): 
            st.session_state.current_page = 'register_page'
            st.experimental_rerun()


    @staticmethod
    def register_page():
        st.header('Register')
        with st.form('Register'):
            c1, c2 = st.columns(2)
            with c1: user = st.text_input('Username')
            with c2: email = st.text_input('Email')

            c1, c2 = st.columns(2)
            with c1: password = st.text_input('Password',type='password')
            with c2: password2 = st.text_input('Repeat Password',type='password')

            if password != password2: st.error('Passwords dont match!')

            if st.form_submit_button('Register',use_container_width=True):
                if password == password2:
                    if Auth.register_user(user,password,email):
                        st.balloons
                        st.info('Sucess')
                        sleep(2)
                        st.session_state.current_page = 'public_page'
                        st.experimental_rerun()

