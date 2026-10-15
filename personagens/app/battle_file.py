def linha(tamanho):
    print('-' * tamanho)

def battle(personagem):
    print('\n')
    linha(40)
    print(f'{"Vamos iniciar o game":^40}')
    linha(40)
    print(f'{"Seja bem-vindo(a)":^40}')
    print(personagem)
    linha(40)
    print()

    cont_ataques = 0
    while True:
        if cont_ataques == 2:
            tot_opcoes = 5
            opcao_jogo = menu_ataques_com_especial(personagem)
            opcao = aplicacao_das_escolhas(opcao_jogo, personagem, tot_opcoes)
            cont_ataques = 0
            if opcao == 0:
                break

        else:
            tot_opcoes = 4
            opcao_jogo = menu_ataques(personagem)
            opcao = aplicacao_das_escolhas(opcao_jogo, personagem, tot_opcoes)
            if opcao == 0:
                break
            elif opcao == 1:
                cont_ataques += 1


def menu_ataques(personagem):
    opcao_jogo = int(input(f'''\n-----> Faça sua escolha <-----
    [ 1 ] - Ver status
    [ 2 ] - {personagem.nome_primeiro_ataque_basico}
    [ 3 ] - {personagem.nome_segundo_ataque_basico}
    [ 0 ] - Sair
Opção: '''))
    return opcao_jogo


def menu_ataques_com_especial(personagem):
    opcao_jogo = int(input(f'''\n-----> Faça sua escolha <-----
    [ 1 ] - Ver status
    [ 2 ] - {personagem.nome_primeiro_ataque_basico}
    [ 3 ] - {personagem.nome_segundo_ataque_basico}
    [ 4 ] - Super: {personagem.nome_da_super}
    [ 0 ] - Sair
Opção: '''))
    return opcao_jogo


def aplicacao_das_escolhas(opcao_jogo, personagem, tot_opcoes):

    if tot_opcoes == 5 and opcao_jogo == 4:
        print(f'Receba a Super {personagem.nome_da_super}')
        return 200 # 'Status code 200 OK'

    if opcao_jogo < 0 or opcao_jogo > 3:
        print('\nOpção inválida. Tente novamente.')
        return None

    if opcao_jogo == 0:
        return 0 # Retorna 0 e causa o break no while de battle

    if opcao_jogo == 1:
        linha(36)
        print(personagem)
        linha(36)
        return 200 # 'Status code 200 OK'

    elif opcao_jogo == 2:
        print(f'\nReceba {personagem.nome_primeiro_ataque_basico}')
        return 1 # Retorna 1 para somar no cont_ataque e fazer a lógica

    elif opcao_jogo == 3:
        print(f'\nReceba {personagem.nome_segundo_ataque_basico}')
        return 1  # Retorna 1 para somar no cont_ataque e fazer a lógica

    return None
