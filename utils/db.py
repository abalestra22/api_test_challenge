""" Module to store database connection. """
import psycopg2
from psycopg2.extras import RealDictCursor

class DBClient:
    def __init__(self, host, dbname, user, password, port=5432):
        self.connection = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )

    def fetch_person_by_id(self, person_id):
        """ Helper function to execute SELECT query against database. """
        query = f"""
            SELECT DISTINCT *
            FROM Test.Worldsys
            WHERE personId = %s;
        """
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (person_id,))
            return cursor.fetchall()

    def close(self):
        """ Helper function to close connection. """
        self.connection.close()
