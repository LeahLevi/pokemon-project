import json
from flask import Flask
import Extension
import pokemon

app = Flask(__name__)

from flask import request

from insert import insert


@app.route('/add_pokemon', methods=["POST"])
def add_pokemon():
    result = request.get_json()
    if pokemon.is_pokemon_already(result):
        return "There is such a Pokemon already", 409
    insert([result])
    return "Pokemon successfully added", 201


@app.route('/delete/<pokemon_id>/<trainer_name>', methods=["DELETE"])
def delete(pokemon_id, trainer_name):
    pokemon.delete(pokemon_id, trainer_name)
    return "Successfully deleted", 201


@app.route('/evolve/<trainer_name>', methods=["PUT"])
def evolve(trainer_name):
    pokemon_id = request.get_json()
    if not pokemon.is_pairs(trainer_name, pokemon_id):
        return "Trainer doesn't have such a Pokémon", 400
    result = pokemon.evolve(trainer_name, pokemon_id)
    if result == "Can't evolve":
        return "Can't evolve", 400

    if result == "this trainer already has this Pokémon":
        return "Can't evolve , this trainer already has this Pokémon", 400
    return "Successfully evolve", 201


@app.route('/war/<trainer1>/<trainer2>', methods=["DELETE"])
def war(trainer1, trainer2):
    return Extension.war(trainer1, trainer2), 200


@app.route('/Get_pokemons_by_trainer/<trainer>', methods=["GET"])
def Get_pokemons_by_trainer(trainer):
    return json.dumps(pokemon.get_pokemons_by_trainer(trainer))


@app.route('/get_status/<trainer1>/<trainer2>', methods=["GET"])
def get_status(trainer1, trainer2):
    return Extension.get_status(trainer1, trainer2), 200


port_number = 3001
if __name__ == '__main__':
    app.run(port=port_number)
