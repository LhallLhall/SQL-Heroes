from database.connection import create_connection
from database.connection import execute_query
# from database.connection import 
def test_is_running():
    assert create_connection("postgres", "postgres", "postgres") == connection

def test_sql():
    execute_query("""
                    SELECT * FROM heroes
                """)
    return 'successful'