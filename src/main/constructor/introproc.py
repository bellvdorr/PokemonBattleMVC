from src.views.fview import intropage
from src.views.atkview import atkpage
from src.datas.dados import pokemons
from src.datas.dados import ataques
from src.main.constructor.introproc import introproc

def introproc():
    command = intropage()
    return command

def atkview():
    command1 = atkpage()
    return command1

def exibeDadosPokemons(n_escolhido):
    for pokemon in pokemons:
        if n_escolhido == pokemon.get("n_pokedex"):
            print("Seu pokemon escolhido foi o", pokemon['nome'], "!")
            return verificaAtaquePokemon(pokemon)
        
def verificaAtaquePokemon(pokemonEscolhido):
    print("Ataques do pokemon")
    for n_ataque in pokemonEscolhido['ataques']:
        for ataque in ataques:
            if n_ataque == ataque['id_ataque']:
                print(ataque['nome_ataque'])
    return 