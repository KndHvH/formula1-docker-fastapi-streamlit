import streamlit as st
import pandas as pd
from service.api_functions import Formula1Data

class Pages:
    @staticmethod
    def main_page():
        drivers_json = Formula1Data.get_driver_data()
        drivers_df = pd.DataFrame(drivers_json["data"], columns=drivers_json["columns"])
        st.dataframe(drivers_df)
    
    @staticmethod
    def public_page():
        drivers_json = Formula1Data.get_driver_data()
        drivers_df = pd.DataFrame(drivers_json["data"], columns=drivers_json["columns"])
        st.dataframe(drivers_df)