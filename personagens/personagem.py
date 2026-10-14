class Personagem:
    def __init__(self, nome, barra_de_vida, escudo, nome_da_super, nome_primeiro_ataque_basico,nome_segundo_ataque_basico):
        self.nome = nome
        self.barra_de_vida = barra_de_vida
        self.escudo = escudo
        self.nome_da_super = nome_da_super
        self.nome_primeiro_ataque_basico = nome_primeiro_ataque_basico
        self.nome_segundo_ataque_basico = nome_segundo_ataque_basico

    def __str__(self):
        classe_pertencente = f'Classe: {self.__class__.__name__}'
        mensagem = f'''{classe_pertencente:^36}
Nome: {self.nome} | Vida: {self.barra_de_vida} | Escudo: {self.escudo}'''

        return f'{mensagem}'

