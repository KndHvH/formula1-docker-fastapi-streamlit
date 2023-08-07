import requests
import os
import streamlit as st
import json

BE_SERVER = os.getenv("BE_SERVER")
BE_PORT = os.getenv("BE_PORT")


#TODO REMOVE
if BE_SERVER is None: BE_SERVER = 'localhost'
if BE_PORT is None: BE_PORT = '8000'


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


class Auth:
    @staticmethod
    def get_token(user,password):
        response = requests.post(
            f"http://{BE_SERVER}:{BE_PORT}/login",
            json={'username':user,'password':password})
        if response.status_code == 200: return response.json()["access_token"],response.status_code
        error_content = json.loads(response.content.decode('utf-8'))
        return error_content.get('detail', 'An error occurred'),response.status_code

    @staticmethod
    def register_user(user,password,email):
        token = f"http://{BE_SERVER}:{BE_PORT}/register"
        response = requests.post(token, json={'username':user,'email':email,'password':password})
        if response.status_code == 200: return 'Success'
        error_content = json.loads(response.content.decode('utf-8'))
        return error_content.get('detail', 'An error occurred')