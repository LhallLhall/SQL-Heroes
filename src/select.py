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
    add_ability_with_id(name)

def add_ability_with_id(name):
    params = (name,)
    query = """
            SELECT id from heroes
            WHERE name = %s
            """
    results = execute_query(query, params).fetchone()[0]
    print(results)

set_main_character() #needed

def set_main_villain():
    name = input('You have turned to the dark side! What is your villain name?: ')
    about = input('Welcome ' + name + '. Now tell me how you became a villain: ')
    bio = input("Don't care. One last question. How did you get your powers?: ")
    params = (name, about, bio)
    query = """
            INSERT INTO villains (name, about_me, biography) VALUES (%s, %s, %s)
            """
    execute_query(query, params)

#set_main_villain() #needed

    
# * add in a function for 

def check_for_abilities_table():
    query = """
            SELECT h.name, att FROM heroes h
            JOIN abilities a ON a.hero_id = h.id
            JOIN ability_types att on a.ability_type_id = att.id;
            """
    # pp(execute_query(query).fetchall())
    list_of_heroes_abilities = execute_query(query).fetchall()
    for x in list_of_heroes_abilities:
        pp(x[0] + " " + x[1])


def player_check_hero_abilities():
    show_heroes_ans = input('Now that we have you registered as an official Superhero would you like to check out (1: Heroes and their abilities OR 2: List of Heroes without their abilities) (type: 1 or 2) ')

    if show_heroes_ans == "1":
        check_for_abilities_table()
    elif show_heroes_ans == "2":
        select_all()
    else:
        print('oops something went wrong')
        player_check_hero_abilities()

#player_check_hero_abilities() # needed

def delete_character():
    input_ans = input("You find yourself against your nemesis (blank for now)! Do you want to attack this villain or run away? But be careful you could either endanger yourself or your fellow heroes (Type: attack/run): ")
    if input_ans == 'attack':
        print("You attack your nemesis and find that your strike is a fatal blow! The villain falls to the ground and your fellow heroes rejoice! You saved the day!")
        query = """
                    DELETE FROM villains
                    WHERE id = 1
                """
        execute_query(query)
    elif input_ans == 'run':
        print("You sprint away in fear not knowing of the villains next move! But as you look back you see them grab another hero. As you rush to save the hero they are ultimately killed by the villain")
        query = """
                    DELETE FROM heroes
                    WHERE id = 28
                """
        execute_query(query)

#delete_character() # needed