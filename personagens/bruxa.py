from personagens.personagem import Personagem


class Bruxa(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 50, 25, 'Necromante',
            'Fire Ball', 'Rajada Umbra')

    def __str__(self):
        return f'Bruxa: {self.nome} | Vida: {self.barra_de_vida} | Escudo: {self.escudo}'

    @staticmethod
    def super_necromante():
        return "Necromante"

    @staticmethod
    def fire_ball():
        return "Fire Ball"

    @staticmethod
    def celeste():
        return "Rajada Umbra"