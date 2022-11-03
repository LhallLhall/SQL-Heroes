from database.connection import execute_query
from pprint import pprint as pp

def select_all():
    query = """
        SELECT * FROM heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    # print(list_of_heroes)
    for record in list_of_heroes:
        pp(record[1])

# select_all()

def set_main_character():
    name = input('Hi Superhero! What should I call you?: ')
    about = input('Hey ' + name + '! I like that name! Tell me a little about your self!: ')
    bio = input("Oh wow! You are a very interesting person! One last question. How did you get your powers?: ")
    params = (name, about, bio)
    query = """
            INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)
            """
    execute_query(query, params)
    # add_ability_with_id(name)

# def add_ability_with_id(name):
#     query = """
#             SELECT id from heroes
#             WHERE name = %s
#             """
#     execute_query(query, name)

set_main_character()

# * add in a function for 

def check_for_abilities_table():
    query = """
            SELECT h.name, att FROM heroes h
            JOIN abilities a ON a.hero_id = h.id
            JOIN ability_types att on a.ability_type_id = att.id;
            """
    pp(execute_query(query).fetchall())
    # list_of_heroes_abilities = execute_query(query).fetchall()
    # for x in list_of_heroes_abilities:
    #     pp(x[0])

# check_for_abilities_table()

def player_check_hero_abilities():
    show_heroes_ans = input('Now that we have you registered as an official Superhero would you like to check out (1: Heroes and their abilities OR 2: List of Heroes without their abilities) (type: 1 or 2) ')

    if show_heroes_ans == "1":
        check_for_abilities_table()
    elif show_heroes_ans == "2":
        select_all()
    else:
        print('oops something went wrong')
        player_check_hero_abilities()

        # alt_ans = input('Would you like to just a list of heroes? (y/n) ')
        # if alt_ans == 
player_check_hero_abilities()
# print('test')