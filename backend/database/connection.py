import os
import psycopg2
import pandas as pd
from psycopg2 import Error
from dotenv import load_dotenv


class DatabaseConnection:
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
            print(f"Erro ao obter conexão com servidor: {error}")
            raise error
        
    def get_dataframe_by_query(self, query):
        connection = self._get_connection()
        with connection:
            if connection is None:
                return None
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query)
                    connection.commit()

                    result = cursor.fetchall()

                    column_names = [desc[0] for desc in cursor.description]
                    df = pd.DataFrame(result, columns=column_names)
                    return df

                except psycopg2.Error as error:
                    self.status = f"Erro ao realizar query: {error}\n---\nquery:{query}"
                    return None
    
    def get_value_by_query(self, query):
        connection = self._get_connection()
        with connection:
            if connection is None: return None
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query)
                    connection.commit()

                    return cursor.fetchone()

                except psycopg2.Error as error:
                    self.status = f"Erro ao realizar query: {error}\n---\nquery:{query}"
                    return None
    


    def insert_values_on_table(self, values, table):
        connection = self._get_connection()
        with connection:
            if connection is None: return None
            with connection.cursor() as cursor:
                try:
                    columns = [column for column in values.keys()]
                    column_values = [values[column] for column in columns]

                    query = f"""
                            INSERT INTO {table} ({','.join(columns)}) 
                            VALUES ({','.join(['%s'] * len(columns))})
                            """
                    
                    cursor.execute(query, column_values)
                    connection.commit()
                    
                except (Exception, Error) as error:
                    self.status = f"Erro ao realizar query: {error}\n---\nquery:{query}"
                    return None

