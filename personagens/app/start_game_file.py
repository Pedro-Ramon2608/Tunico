from .. import pergunta_nome_personagem
from ..arqueiro import Arqueiro
from ..bruxa import Bruxa
from ..paladino import Paladino
from .battle_file import battle

def start_game():
    while True:
        opcao_personagem = int(input('''\n-----> Escolha seu Personagem <-----
    [ 1 ] - Arqueiro
    [ 2 ] - Bruxa
    [ 3 ] - Paladino
    [ 0 ] - Sair
Opção: '''))

        if opcao_personagem < 0 or opcao_personagem > 3:
            print('\nOpção inválida. Tente novamente.')
            continue

        if opcao_personagem == 0:
            break

        elif opcao_personagem == 1:
            nome_usuario = pergunta_nome_personagem()
            personagem = Arqueiro(nome=nome_usuario)
            battle(personagem)

        elif opcao_personagem == 2:
            nome_usuario = pergunta_nome_personagem()
            personagem = Bruxa(nome=nome_usuario)
            battle(personagem)

        elif opcao_personagem == 3:
            nome_usuario = pergunta_nome_personagem()
            personagem = Paladino(nome=nome_usuario)
            battle(personagem)