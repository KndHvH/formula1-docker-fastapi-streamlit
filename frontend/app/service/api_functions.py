import requests
import os
import streamlit as st

BE_SERVER = os.getenv("BE_SERVER")
BE_PORT = os.getenv("BE_PORT")


class Formula1Data:
    
    @staticmethod
    def get_driver_data():
        response = requests.get(f"http://{BE_SERVER}:{BE_PORT}/drivers")
        data = response.json()
        return data

    @staticmethod
    def get_race_data():
        response = requests.get(f"http://{BE_SERVER}:{BE_PORT}/races")
        data = response.json()
        return data

    @staticmethod
    def get_fastest_laps_data():
        response = requests.get(f"http://{BE_SERVER}:{BE_PORT}/fastest_laps")
        data = response.json()
        return data
