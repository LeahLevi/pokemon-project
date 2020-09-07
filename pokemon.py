import pymysql
import requests
from flask import request

import pokeAPI
from insert import insert

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def is_pokemon_already(result):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from pokemon where id = {result['id']}")
        if cursor.fetchall():
            return True
        return False

#
# def insert_pokemon(result):
#     tmp = [result]
#     insert(tmp)


def delete(pokemon_id, trainer_name):
    with connection.cursor() as cursor:
        query = f"delete from pokemon_trainer where tname = \"{trainer_name}\" and pid = \"{pokemon_id}\";"
        cursor.execute(query)
        connection.commit()


def is_pairs(trainer_name,pokemon_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select tname from pokemon_trainer where pid = {pokemon_id} and tname = '{trainer_name}'")
        if cursor.fetchall():
            return True

def evolve(trainer_name,pokemon_id):
    with connection.cursor() as cursor:
        info = pokeAPI.get_info(pokemon_id)
        cursor.execute(f"select name from pokemon where id = {pokemon_id}")
        res = cursor.fetchone()
        tmp = info["chain"]
        while tmp["species"]["name"] != res["name"]:
            tmp = tmp["evolves_to"][0]
        if not tmp.get('evolves_to'):
            return "Can't evolve"
        cursor.execute(f"select id from pokemon where name = '{tmp['evolves_to'][0]['species']['name']}'")
        id = cursor.fetchone()
        if is_pairs(trainer_name,id['id']):
            return "this trainer already has this Pokémon"
        cursor.execute(f"update pokemon_trainer set pid = {id['id']} where tname = '{trainer_name}' and pid = {pokemon_id}")
        connection.commit()

def Get_name_pokemons_by_trainer(trainer):
    with connection.cursor() as cursor:
        query = f"select pokemon.name from pokemon_trainer,pokemon where pokemon_trainer.tname = '{trainer}' and " \
                f"pokemon_trainer.pid = pokemon.id "
        cursor.execute(query)
        res = cursor.fetchall()
        return [x['name'] for x in res]


def get_pokemons_by_trainer(trainer):
    with connection.cursor() as cursor:
        cursor.execute(
        f"select * from pokemon where id in (select pid from pokemon_trainer where tname = '{trainer}')")
        return cursor.fetchall()

def get_pokemon_from_war(trainer):
    with connection.cursor() as cursor:
        cursor.execute( f"select pokemon from war where trainer = '{trainer}'")
        return cursor.fetchone()