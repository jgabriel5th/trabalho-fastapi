class Escola:
    def __init__(self, nome_escola: str, fundacao: int, setor: str):
        self.nome_escola = nome_escola
        self.fundacao = fundacao
        self.setor = setor
        self._professores = []
        self.sala_aula = []

    def adicionar_sala(self, numero_sala: int, bloco: str):
            sala = SalaDeAula(numero_sala, bloco)
            self.sala_aula.append(sala)
    
    def informacao_salas(self):
        for sala in self.sala_aula:
            print(f'Número da sala: {sala.numero_sala}\nBloco: {sala.bloco}')

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

    def informacao_escola(self):
            print(f'Nome da escola: {self.nome_escola}\nAno da fundação: {self.fundacao}\nSetor: {self.setor}')

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

class SalaDeAula:
    def __init__(self, numero_sala: int, bloco: str):
        self.numero_sala = numero_sala
        self.bloco = bloco


class Aluno:
    def __init__(self, nome, idade, genero, estudando=False):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.estudando = estudando
        self.enderecos = []

    def estudar(self):
        if self.estudando:
            print(f'{self.nome} já está estudando...')
            return

        print(f'{self.nome} está estudando...')
        self.estudando = True

    def parar_estudar(self):
        if not self.estudando:
            print(f'{self.nome} já parou de estudar...')
            return

        self.estudando = False
        print(f'{self.nome} parou de estudar...')

    def adicionar_endereco(self, rua, bairro, numero):
        self.enderecos.append(Endereco(rua, bairro, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(f'Rua: {endereco.rua}\nBairro: {endereco.bairro}\nNúmero: {endereco.numero}')

    
class Endereco:
    def __init__(self, rua, bairro, numero):
        self.rua = rua
        self.bairro = bairro
        self.numero = numero



    


escola1 = Escola('CEV', 2015, 'Privado')
escola1.adicionar_sala(123, 'C')
escola1.informacao_salas()
escola1.informacao_escola()
professor1 = Professor('John', 25, 'Biologia', 'Masculino')
professor1.ensinar()
escola1.adicionar_professor(professor1)
escola1.ensinar_professor(professor1)
escola1.informacao_professor()
aluno1 = Aluno('Gabriel', 21, 'Masculino')
aluno1.estudar()
aluno1.estudar()
aluno1.parar_estudar()
aluno1.parar_estudar()
aluno1.adicionar_endereco('Rua teste', 'Bairro teste', 234)
aluno1.listar_endereco()