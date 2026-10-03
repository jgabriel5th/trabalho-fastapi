class Professor:
    def __init__(self, nome: str, idade: int, disciplina: str, genero: str):
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina
        self.genero = genero
        self._escola = None

    @property
    def escola(self):
        return self._escola

    @escola.setter
    def escola(self, valor):
        self._escola = valor

    def ensinar(self):
        if self._escola is not None:
            print(f'Ensinando {self.disciplina} em {self._escola}')
        else:
            print(f'{self.nome} está sem escola para ensinar')


class Escola:
    def __init__(self, nome_escola: str, fundacao: int, setor: str):
        self.nome_escola = nome_escola
        self.fundacao = fundacao
        self.setor = setor
        self.professores = []

    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)

    def informacao_professor(self):
        for index, professor in enumerate(self.professores):
            print(f'Professor {index +1}: {professor.nome}\nDisciplina: {professor.disciplina}')

    def remover_professor(self, nome_professor: str):
        self.professores.remove(nome_professor)

    def __str__(self):
        return self.nome_escola

    


professor1 = Professor('Coelho', 32, 'Programação', 'Homem')
professor2 = Professor('Everton', 33, 'Programação', 'Homem')
escola1 = Escola('Liceu', 1927, 'Público')
professor1.escola = escola1
professor2.escola = escola1
escola1.adicionar_professor(professor1)
escola1.adicionar_professor(professor2)
escola1.informacao_professor()
escola1.remover_professor(professor1)
# escola1.informacao_professor()
escola1.remover_professor(professor2)
escola1.informacao_professor()