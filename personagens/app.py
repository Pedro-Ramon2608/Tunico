from personagens import linha, perguntas_basicas
from personagens.arqueiro import Arqueiro
from personagens.bruxa import Bruxa
from personagens.paladino import Paladino

def start_game():
    while True:
        opcao_personagem = int(input('''-----> Escolha seu Personagem <-----
    [ 1 ] - Arqueiro
    [ 2 ] - Bruxa
    [ 3 ] - Paladino
    [ 0 ] - Sair
Opção: '''))

        if opcao_personagem < 0 or opcao_personagem > 3:
            print('Opção inválida. Tente novamente.')
            continue

        if opcao_personagem == 0:
            break

        elif opcao_personagem == 1:
            nome_usuario = perguntas_basicas()
            personagem = Arqueiro(nome=nome_usuario)
            battle(personagem)

        elif opcao_personagem == 2:
            nome_usuario = perguntas_basicas()
            personagem = Bruxa(nome=nome_usuario)
            battle(personagem)

        elif opcao_personagem == 3:
            nome_usuario = perguntas_basicas()
            personagem = Paladino(nome=nome_usuario)
            battle(personagem)


def battle(personagem):
    print('\n')
    linha(40)
    print(f'{"Vamos iniciar o game":^40}')
    linha(40)
    print(f'{"Seja bem-vindo(a)":^40}')
    print(personagem)
    linha(40)
    print()
    while True:
        opcao_jogo = int(input(f'''-----> Faça sua escolha <-----
    [ 1 ] - Ver status
    [ 2 ] - {personagem}
    [ 0 ] - Sair
Opção: '''))
