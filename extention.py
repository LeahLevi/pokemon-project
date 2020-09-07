import random
from flask import Flask, Response

from pokemon import pokeAPI
from pokemon.db_models import pokemon, trainer

app = Flask(__name__)

def get_power(pokemon):
    base_experience_1 = pokeAPI.get_base_experience(pokemon["id"])
    height_1 = (pokemon["height"])
    weight_1 = (pokemon["weight"])
    power = base_experience_1 * height_1 / weight_1
    return power


@app.route("/war/<trainer_1>/<trainer_2>", methods=["DELETE"])
def war(trainer_1, trainer_2):
    # if not trainer.is_exist(trainer_1):
    #     return Response(f"{trainer_1} don't have any pokemon")
    # if not trainer.is_exist(trainer_2):
    #     return Response(f"{trainer_2} don't have any pokemon")
    pt1 = pokemon.get_pokemon(trainer_1)
    pt2 = pokemon.get_pokemon(trainer_2)
    while pt1 and pt2:
        choice_1 = random.choice(pt1)
        choice_2 = random.choice(pt2)
        print(choice_1, choice_2)
        power_1 = get_power(choice_1)
        power_2 = get_power(choice_2)
        print(power_1, power_2)
        if power_1 > power_2:
            pokemon.delete(choice_2["name"], trainer_2)
        else:
            pokemon.delete(choice_1["name"], trainer_1)

    if pt1:
        return Response(f"'{trainer_2}' is the winner!!!!!!!!")
    return Response(f"'{trainer_1}' is the winner!!!!!!!!")





port_number = 4000
if __name__ == '__main__':
    app.run(port=port_number)

