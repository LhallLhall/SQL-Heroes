from database.connection import execute_query
from pprint import pprint as pp

def select_all():
    query = """
        SELECT * FROM heroes
    """

    list_of_heroes = execute_query(query).fetchall()
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
    add_ability_with_id(name, 'heroes')
    create_main_villain(name)
    # change_name(name)

def add_ability_with_id(name, table_name=None):
    query_str = "SELECT id from " + table_name;
    query = query_str + """
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
            INSERT INTO villains (name, about_me, biography) VALUES (%s, %s, %s)
            """
    execute_query(query, params)
    # add_ability_with_id(name, 'villains')
    player_check_hero_abilities()
    delete_character(hero_name, name)

#create_main_villain() #needed

def check_for_abilities_table():
    query = """
            SELECT h.name, att.name FROM heroes h 
            JOIN abilities a ON a.hero_id = h.id
            JOIN ability_types att on a.ability_type_id = att.id;
            """
    # pp(execute_query(query).fetchall())
    list_of_heroes_abilities = execute_query(query).fetchall()
    for x in list_of_heroes_abilities:
        pp(x[0] + " : " + x[1])

def check_for_villain_abilities_table():
    query = """
            SELECT v.name, att.name FROM villains v 
            JOIN abilities a ON a.hero_id = v.id
            JOIN ability_types att on a.ability_type_id = att.id;
            """
    # pp(execute_query(query).fetchall())
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

 #needed

#player_check_hero_abilities() # needed

# def change_name(name):
#     change_name_ans = input("Before you go out crime fighting would you like to change your name to disguise yourself?: (y/n)")
#     if change_name_ans == 'y':
#         name_change = input("What would you like it to be?: ")
#         query = """
#                 SELECT name from heroes
#                 WHERE name = %s
#                 """
#         execute_query(query, name_change)


def delete_character(hero_name, villain_name):
    input_ans = input("You find yourself against your nemesis " + villain_name + "! Do you want to attack this villain or run away? But be careful you could either endanger yourself or your fellow heroes (Type: attack/run): ")
    if input_ans == 'attack':
        # blah = input('Are you sure you want to attack? ' + villain_name)
        print("You attack your nemesis and find that your strike is a fatal blow! The villain falls to the ground and your fellow heroes rejoice! You saved the day!")
        import_id_num = """
                        SELECT id from villains
                        WHERE name = %s
                        """
        villain_id = execute_query(import_id_num, (villain_name,) ).fetchone()[0]
        query = """
                DELETE from villains
                WHERE id = %s
                """
        execute_query(query, (villain_id,))
    elif input_ans == 'run':
        print("You sprint away in fear not knowing of the villains next move! But as you look back you see them grab another hero. As you rush to save the hero they are ultimately killed by the villain")
        query = """
                    SELECT id from heroes
                    WHERE name = %s
                    DELETE FROM heroes
                    WHERE id = 28
                """
        execute_query(query)

#delete_character() # needed

set_main_character() # needed