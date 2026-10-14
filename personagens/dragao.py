from personagens.personagem import Personagem


class Dragao(Personagem):
    def __init__(self):
        super().__init__('Tunico', 1_000, 300, 'Garra Mortal',
                         'Sopro Dracônico', 'Draco Meteor')
    def __str__(self):
        return f'Dragão: {self.nome} | Vida: {self.barra_de_vida} | Escudo: {self.escudo}'

    @staticmethod
    def garra_mortal():
        return "Garra Mortal"

    @staticmethod
    def sopro_draconico():
        return "Sopro Dracônico"

    @staticmethod
    def super_draco_meteoro():
        return "Draco Meteor"
