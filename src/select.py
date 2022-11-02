from database.connection import execute_query

def select_all():
    query = """
        SELECT * FROM heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    # print(list_of_heroes)
    for record in list_of_heroes:
        print(record[1])

select_all()

# print('test')