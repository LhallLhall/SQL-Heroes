import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        return cursor
    except OSError as err:
        print(f"The error '{e}' occurred or the hero name is already taken")
    
create_connection('postgres', "postgres", "postgres")

# DONT EDIT ABOVE THIS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def select_all():
#     query = """
#         SELECT * FROM heroes
#     """

#     list_of_heroes = execute_query(query).fetchall()
#     # print(list_of_heroes)
#     for record in list_of_heroes:
#         print(record[1])

# select_all()

def set_main_character():
    name = input('Hi SuperHero! What should I call you?: ')
    about = input('I like that name! Tell me a little about your self!: ')
    bio = input("Oh wow! You are a very interesting person! One last question. How did you get your powers?: ")
    params = (name, about, bio)
    query = """
            INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)
            """
    execute_query(query, params)

set_main_character()