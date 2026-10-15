from personagens import linha, pergunta_nome_personagem
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


cont_ataques = 0

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
        if cont_ataques == 2:
            opcao_jogo = menu_ataques_com_especial(personagem)
            opcao = aplicacao_das_escolhas(opcao_jogo, personagem)
            cont_ataques = 0
            if opcao == 0:
                break

        else:
            opcao_jogo = menu_ataques(personagem)
            opcao = aplicacao_das_escolhas(opcao_jogo, personagem)
            if opcao == 0:
                break


def menu_ataques(personagem):
    opcao_jogo = int(input(f'''-----> Faça sua escolha <-----
        [ 1 ] - Ver status
        [ 2 ] - {personagem.nome_primeiro_ataque_basico}
        [ 3 ] - {personagem.nome_segundo_ataque_basico}
        [ 0 ] - Sair
    Opção: '''))
    return opcao_jogo

def menu_ataques_com_especial(personagem):
    opcao_jogo = int(input(f'''-----> Faça sua escolha <-----
        [ 1 ] - Ver status
        [ 2 ] - {personagem.nome_da_super}
        [ 3 ] - {personagem.nome_primeiro_ataque_basico}
        [ 4 ] - {personagem.nome_segundo_ataque_basico}
        [ 0 ] - Sair
    Opção: '''))
    return opcao_jogo

def aplicacao_das_escolhas(opcao_jogo, personagem):
    if opcao_jogo < 0 or opcao_jogo > 3:
        return 'Opção inválida. Tente novamente.'

    if opcao_jogo == 0:
        return 0

    if opcao_jogo == 1:
        return linha(36) + '\n' + print(personagem) + '\n' + linha(36)

    elif opcao_jogo == 2:
        cont_ataques += 1
        return f'Receba {personagem.nome_primeiro_ataque_basico}'

    elif opcao_jogo == 3:
        cont_ataques += 1
        return f'Receba {personagem.nome_segundo_ataque_basico}'
