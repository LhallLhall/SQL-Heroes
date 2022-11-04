from database.connection import execute_query
from pprint import pprint as pp

def select_all_heroes():
    query = """
        SELECT * FROM heroes
        WHERE is_villain = false
    """

    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record[1])

def select_all_villains():
    query = """
        SELECT * FROM heroes
        WHERE is_villain = true
    """

    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record[1])

def set_main_character():
    name = input('Hi Superhero! What should I call you?: ')
    about = input('Hey ' + name + '! I like that name! Tell me a little about your self!: ')
    bio = input("Oh wow! You are a very interesting person! One last question. How did you get your powers?: ")
    params = (name, about, bio)
    query = """
            INSERT INTO heroes (name, about_me, biography, is_villain) VALUES (%s, %s, %s, false)
            """
    execute_query(query, params)
    add_ability_with_id(name)
    create_main_villain(name)

def add_ability_with_id(name):
    query = """
            SELECT id from heroes
            WHERE name = %s
            """
    results = execute_query(query, (name,)).fetchone()[0]

    print(results)
    type_id = input('What is your super power? 1: Super Strength 2: Flying 3: Telekinesis 4: Telepathy: 5: Frost Breath 6: Super Speed 7: Super Vision. Type(1-7): ')
    ability_params = (results, int(type_id))
    adding_ability = """
                    INSERT INTO abilities (hero_id, ability_type_id) VALUES (%s, %s)
                    """
    updated_table = execute_query(adding_ability, ability_params)
    print(updated_table)

def create_main_villain(hero_name):
    name = input('* Now at the lair of the "Order of the Villains" * Ah welcome to the order of the villains! What is your villain name?: ')
    about = input('Welcome ' + name + '. Now tell me how you became a villain: ')
    bio = input("One last question. How did you get your powers?: ")
    params = (name, about, bio)
    query = """
            INSERT INTO heroes (name, about_me, biography, is_villain) VALUES (%s, %s, %s, true)
            """
    execute_query(query, params)
    add_ability_with_id(name)
    player_check_hero_abilities()
    delete_character(hero_name, name)

def check_for_abilities_table():
    query = """
            SELECT h.name, att.name FROM heroes h 
            JOIN abilities a ON a.hero_id = h.id
            JOIN ability_types att on a.ability_type_id = att.id;
            """
    list_of_heroes_abilities = execute_query(query).fetchall()
    for x in list_of_heroes_abilities:
        pp(x[0] + " : " + x[1])

def check_for_villain_abilities_table():
    query = """
            SELECT v.name, att.name FROM heroes v 
            JOIN abilities a ON a.hero_id = v.id
            JOIN ability_types att on a.ability_type_id = att.id
            WHERE v.is_villain = true;
            """
    list_of_villains_abilities = execute_query(query).fetchall()
    for x in list_of_villains_abilities:
        pp(x[0] + " : " + x[1])


def player_check_hero_abilities():
    show_heroes_ans = input('Now that we have you registered as an official Superhero would you like to check out (1: Heroes and their abilities OR 2: List of Villains and their abilities) (type: 1 or 2) ')

    if show_heroes_ans == "1":
        check_for_abilities_table()
    elif show_heroes_ans == "2":
        check_for_villain_abilities_table()
    else:
        print('oops something went wrong')
        player_check_hero_abilities()

def villain_conversion_therapy(name):
    print("The Villain realizes what he is doing is wrong and suddenly has a change of heart. The Villain signs up for 'Villain Conversion Therapy'")
    query = """
            SELECT id from heroes
            WHERE name = %s
            """
    results = execute_query(query, (name,)).fetchone()[0]
    
    query = """
            UPDATE heroes
            SET is_villain = false
            WHERE id = %s
            """
    execute_query(query, (results,))
    check_for_villain_abilities_table()


def delete_character(hero_name, villain_name):
    input_ans = input("You find the villain " + villain_name + " trashing the town! Do you want to attack this villain or run away? (Type: attack/run): ")
    if input_ans == 'attack':
        print("You attack your nemesis and find that your strike is a fatal blow! The villain falls to the ground and your fellow heroes rejoice! You saved the day!")
        import_id_num = """
                        SELECT id from heroes
                        WHERE name = %s AND is_villain = true
                        """
        villain_id = execute_query(import_id_num, (villain_name,) ).fetchone()[0]
        query = """
                DELETE from heroes
                WHERE id = %s
                """
        execute_query(query, (villain_id,))
    elif input_ans == 'run':
        print('You sprint away in waiting for the villain to get tired. But you see something happen to them. It looks like they have had a realization.')
        villain_conversion_therapy(villain_name)
        
        

set_main_character() # needed