import streamlit as st
import pandas as pd
from service.api_functions import ApiFunctions

drivers_json = ApiFunctions.get_driver_data()
drivers_df = pd.DataFrame(drivers_json['data'], columns=drivers_json['columns'])
st.dataframe(drivers_df)

