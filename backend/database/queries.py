from database.connection import DatabaseConnection
from auth.auth import Auth
from auth.models import User


class ContentQueries:
    @staticmethod
    def get_drivers_json():
        conn = DatabaseConnection()
        query = "SELECT * FROM drivers"
        df = conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")

    @staticmethod
    def get_fastest_laps_json():
        conn = DatabaseConnection()
        query = "SELECT * FROM fastest_laps"
        df = conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")

    @staticmethod
    def get_races_json():
        conn = DatabaseConnection()
        query = "SELECT * FROM races"
        df = conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")


class AuthQueries:

    @staticmethod
    def get_user_and_hash_by_username(username):
        conn = DatabaseConnection()
        query = f"SELECT dsc_username, dsc_password_hash FROM users WHERE dsc_username = '{username}'"
        result = conn.get_value_by_query(query)
        if result: return {'username':result[0],'hash':result[1]}
    
    @staticmethod
    def create_user(user: User):
        conn = DatabaseConnection()

        hash = Auth.get_password_hash(password=user.password)

        values = {
            "DSC_USERNAME": user.username,
            "DSC_EMAIL": user.email,
            "DSC_PASSWORD_HASH": hash
        }

        result = conn.insert_values_on_table(values,'USERS')
        return result