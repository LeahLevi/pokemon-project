import json
import pymysql

data = open("data.json")
pokemon_data = json.load(data)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="963741",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def into_list(data):
    result = []
    for res in data:
        result.append(res['name'])
    return result

def max_weight():
    try:
        with connection.cursor() as cursor:
            query = f"select * from pokemon where weight = (select max(weight) from pokemon)".format()
            cursor.execute(query)
            return cursor.fetchall()
    except:
        print("ERROR")


def find_by_type(p_type):
    try:
        with connection.cursor() as cursor:
            query = f"select name from pokemon where type = '{p_type}'"
            cursor.execute(query)
            return into_list(cursor.fetchall())
    except:
        print("ERROR")


def find_owners(p_name):
    try:
        with connection.cursor() as cursor:
            query = f"select trainer.name from pokemon join trainer join pokemon_trainer on pokemon.id = pid and " \
                    f"trainer.id = tid where '{p_name}' = pokemon.name "
            cursor.execute(query)
            return into_list(cursor.fetchall())
    except:
        print("ERROR")


def find_roster(t_name):
    try:
        with connection.cursor() as cursor:
            query = f"select pokemon.name from pokemon join trainer join pokemon_trainer on pokemon.id = pid and " \
                    f"trainer.id = tid where '{t_name}' = trainer.name "
            cursor.execute(query)
            return into_list(cursor.fetchall())
    except:
        print("ERROR")


def find_max():
    with connection.cursor() as cursor:
        query = f"select tid from pokemon_trainer where count(tid) = max(count(tid))"

print(max_weight())
print(find_by_type("grass"))
print(find_owners("gengar"))
print(find_roster("Loga"))
