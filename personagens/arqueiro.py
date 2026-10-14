from personagens.personagem import Personagem


class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 45, 25, 'Vendaval de Flechas',
            'Flecha Explosiva', 'Mira Certa')

    @staticmethod
    def super_vendaval_de_flechas():
        return 'Vendaval de Flechas'

    @staticmethod
    def flecha_explosiva():
        return 'Flecha Explosiva'

    @staticmethod
    def mira_certa():
        return 'Mira Certa'
