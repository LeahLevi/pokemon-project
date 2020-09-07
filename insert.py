import json
import pymysql




connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("the connection is opened")


def insert_to_pokemon(pokemon_data):
    with connection.cursor() as cursor:
        for i in pokemon_data:
            query = f"insert into pokemon values ({i['id']},'{i['name']}',{i['height']},{i['weight']})"
            cursor.execute(query)
            connection.commit()

def insert_to_trainer(pokemon_data):
    with connection.cursor() as cursor:
        for x in pokemon_data:
            for y in x["ownedBy"]:
                query = f"select count(*) from trainer where '{y['name']}' = name and '{y['town']}' = town "
                cursor.execute(query)
                res = cursor.fetchone()
                if not res['count(*)']:
                    query = f"insert into trainer(name, town) values ('{y['name']}','{y['town']}')"
                    cursor.execute(query)
                    connection.commit()

def insert_to_P_T(pokemon_data):
    with connection.cursor() as cursor:
        for x in pokemon_data:
            for y in x["ownedBy"]:
                tmp = f"select name from trainer where name = '{y['name']}' and town = '{y['town']}'"
                cursor.execute(tmp)
                xid = x['id']
                cursname = cursor.fetchone()['name']
                query = f"insert into pokemon_trainer(pid, tname) values ({xid},'{cursname}')"
                cursor.execute(query)
                connection.commit()


def insert_to_type(pokemon_data):
    with connection.cursor() as cursor:
        for x in pokemon_data:
            query = f"select count(*) from type where '{x['type']}' = name"
            cursor.execute(query)
            res = cursor.fetchone()
            if not res['count(*)']:
                print(x)
                query = f"insert into type(name) values ('{x['type']}')"
                cursor.execute(query)
                connection.commit()

def insert_to_pokemons_type(pokemon_data):
    with connection.cursor() as cursor:
        for x in pokemon_data:
            cursor.execute(f"insert into pokemon_types(pid, tname) values ({x['id']},'{x['type']}')")
            connection.commit()


def insert(pokemon_data):
    insert_to_pokemon(pokemon_data)
    insert_to_trainer(pokemon_data)
    insert_to_P_T(pokemon_data)
    insert_to_type(pokemon_data)
    insert_to_pokemons_type(pokemon_data)




the_file = open("pokemon_data.json")
pokemon_data = json.load(the_file)
# insert(pokemon_data)
