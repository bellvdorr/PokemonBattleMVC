from .constructor.introproc import introproc, exibeDadosPokemons,verificaAtaquePokemon

def start() -> None:

    while True:
        command = introproc()
        
        if command == '1':
            exibeDadosPokemons(1)
            
        elif command == '2':
            exibeDadosPokemons(2)
           
        elif command == '3':
            exibeDadosPokemons(3)

        elif command == '4':
            exit()
        elif command <= '0' or command > '4':
            print('\n COMANDO INVALIDO!!!\n\n')