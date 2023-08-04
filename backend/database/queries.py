import pandas as pd
from database.connection import DatabaseConnection


class TableQueries:
    @staticmethod
    def get_drivers_json():
        f1conn = DatabaseConnection()
        query = "SELECT * FROM drivers"
        df = f1conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")

    @staticmethod
    def get_fastest_laps_json():
        f1conn = DatabaseConnection()
        query = "SELECT * FROM fastest_laps"
        df = f1conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")

    @staticmethod
    def get_races_json():
        f1conn = DatabaseConnection()
        query = "SELECT * FROM races"
        df = f1conn.get_dataframe_by_query(query)
        return df.to_dict(orient="split")
