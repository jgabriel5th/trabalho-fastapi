class Escola:
    def __init__(self, nome_escola: str, ano_fundacao: int, setor: str):
        self.nome_escola = nome_escola
        self.ano_fundacao = ano_fundacao
        self.setor = setor
        self.sala_aula = []

    def adicionar_sala(self, numero_sala: int, bloco: str):
        self.sala_aula.append(SalaDeAula(numero_sala, bloco))

    def informacao_salas(self):
        for sala in self.sala_aula:
            print(f'Número da sala: {sala.numero_sala}\nBloco: {sala.bloco}')

    def informacao_escola(self):
        print(f'Nome da escola: {self.nome_escola}\nAno da fundação: {self.ano_fundacao}\nSetor: {self.setor}')


class SalaDeAula:
    def __init__(self, numero_sala: int, bloco: str):
        self.numero_sala = numero_sala
        self.bloco = bloco

escola1 = Escola('Liceu', 1927, 'Público')
escola1.adicionar_sala(207, 'B')
escola1.informacao_escola()
escola1.informacao_salas()