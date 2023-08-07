import streamlit as st
from cache.session_state import SessionState
from widgets.pages import Pages

SessionState.init_session_state()

match st.session_state.current_page:
    case 'public_page': Pages.public_page()
    case 'main_page': Pages.main_page()
    case 'login_page': Pages.login_page()
    case 'register_page': Pages.register_page()
