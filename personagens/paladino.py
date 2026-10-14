from personagens.personagem import Personagem


class Paladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 75, 25, 'Benção Divina',
                         'Espada de Luz', 'Corte Rápido')

    def __str__(self):
        return f'Paladino: {self.nome} | Vida: {self.barra_de_vida} | Escudo: {self.escudo}'

    @staticmethod
    def super_bencao_divina():
        return "Benção Divina"

    @staticmethod
    def espada_de_luz():
        return "Espada de Luz"

    @staticmethod
    def tramontina():
        return "Corte Rápido"
