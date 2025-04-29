from src.views.fview import intropage
from src.datas.dados import pokemons
from src.datas.dados import ataques

def introproc():
    command = intropage()
    return command

def exibeDadosPokemons(n_escolhido):
    for pokemon in pokemons:
        if n_escolhido == pokemon.get("n_pokedex"):
            return print("Seu pokemon escolhido foi o", pokemon['nome'], "!")

