import os
import psycopg2
import pandas as pd
from psycopg2 import Error
from dotenv import load_dotenv

class F1DatabaseConnection:
    def __init__(self) -> None:
        self.status = "OK"

    def _get_connection(self):
        load_dotenv()
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_SERVER"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_DATABASE"),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD"),
            )
            return connection

        except psycopg2.Error as error:
            self.status = f"Erro ao obter conexão com servidor: {error}"
            return None

    def get_dataframe_by_query(self, query):
        with self._get_connection() as connection:
            if connection is None: return None
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query)
                    connection.commit()

                    try:
                        result = cursor.fetchall()
                    except psycopg2.Error:
                        result = None

                    column_names = [desc[0] for desc in cursor.description]
                    df = pd.DataFrame(result, columns=column_names)
                    return df

                except psycopg2.Error as error:
                    self.status = f"Erro ao realizar query: {error}\n---\nquery:{query}"
                    return None
