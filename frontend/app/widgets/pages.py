from time import sleep
import json
import streamlit as st
import pandas as pd
from service.api_functions import Formula1Data, Auth

class Pages:
    @staticmethod
    def main_page():
        st.code(st.session_state.token)
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
                token,status_code = Auth.get_token(user,password)
                match status_code:
                    case 200:
                        st.session_state.token = token
                        st.session_state.current_page = 'main_page'
                        st.experimental_rerun()
                    case _:
                        st.error(token)
        if st.button('Register',use_container_width=True): 
            st.session_state.current_page = 'register_page'
            st.experimental_rerun()


    @staticmethod
    def register_page():
        st.header('Register')
        with st.form('Register'):
            error = False

            c1, c2 = st.columns(2)
            with c1: user = st.text_input('Username')
            with c2: email = st.text_input('Email')

            c1, c2 = st.columns(2)
            with c1: password = st.text_input('Password',type='password')
            with c2: password2 = st.text_input('Repeat Password',type='password')
            

            error = password == '' or user == '' or password != password2

            if st.form_submit_button('Register',use_container_width=True):
                if not error: 
                    response = Auth.register_user(user,password,email)
                    match response:
                        case 'Success':
                            st.balloons
                            st.info('Sucess')
                            sleep(2)
                            st.session_state.current_page = 'public_page'
                            st.experimental_rerun()

                        case _: st.error(response)
                                            

                if password == '' or user == '': st.error('Empty field')
                if password != password2: st.error('Passwords dont match')
                    
