class Escola:
    def __init__(self, nome_escola: str, fundacao: int, setor: str):
        self.nome_escola = nome_escola
        self.fundacao = fundacao
        self.setor = setor
        self._professores = []

    def adicionar_professor(self, *professores):
        self._professores += professores

    def informacao_professor(self):
        for index, professor in enumerate(self._professores):
            print(f'Professor {index +1}: {professor.nome}\nDisciplina: {professor.disciplina}')

    def remover_professor(self, professor: Professor):
        self._professores.remove(professor)

    def ensinar_professor(self, professor: Professor):
        if professor in self._professores:
            print(f'{professor.nome} ensina {professor.disciplina} em {self.nome_escola}')
        else:
            print('Professor não encontrado')

    def __str__(self):
        return self.nome_escola

class Professor:
    def __init__(self, nome: str, idade: int, disciplina: str, genero: str):
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina
        self.genero = genero


    def ensinar(self):
        print(f'{self.nome} ensina {self.disciplina}')



    


professor1 = Professor('Coelho', 32, 'Programação', 'Homem')
professor2 = Professor('Everton', 33, 'Programação', 'Homem')
escola1 = Escola('Liceu', 1927, 'Público')
escola1.adicionar_professor(professor1)
escola1.adicionar_professor(professor2)
escola1.ensinar_professor(professor1)
professor1.ensinar()
