import streamlit as st

class SessionState:
    @staticmethod
    def init_session_state():
        if 'token' not in st.session_state:
            st.session_state.token = None
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'public_page'
        