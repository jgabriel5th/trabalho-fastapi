from datetime import date

class Veiculo:
    def __init__(self, placa: str, modelo: str, ano: int, valor_diaria: float):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def alterar_status_disponibilidade(self, status: bool):
        self.disponivel = status


class Condutor:
    def __init__(self, nome: str, numero_cnh: str):
        self.nome = nome
        self.numero_cnh = numero_cnh

    def exibir_dados(self):
        return f"Condutor: {self.nome} | CNH: {self.numero_cnh}"


class ContratoLocacao:
    def __init__(self, data_inicio: date, data_termino: date, cliente_nome: str, veiculo: Veiculo, nome_condutor: str, cnh_condutor: str):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.cliente_nome = cliente_nome
        self.status = "ativo"
        
        # AGREGACÃO: O veículo já existe e é recebido por parâmetro
        self.veiculo = veiculo
        self.veiculo.alterar_status_disponibilidade(False)

        # COMPOSIÇÃO: O Condutor é instanciado DENTRO do contrato (ciclo de vida atrelado)
        self.condutor = Condutor(nome=nome_condutor, numero_cnh=cnh_condutor)

    def resumo_contrato(self):
        return (
            f"--- Contrato de Locação ---\n"
            f"Cliente: {self.cliente_nome}\n"
            f"Veículo: {self.veiculo.modelo} ({self.veiculo.placa})\n"
            f"{self.condutor.exibir_dados()}\n"
            f"Status: {self.status}"
        )

if __name__ == "__main__":
    # Instanciando um veículo (Agregação)
    carro1 = Veiculo(placa="ABC-1234", modelo="Civic", ano=2023, valor_diaria=200.0)

    # Criando o contrato (O Condutor é criado internamente via Composição)
    contrato = ContratoLocacao(
        data_inicio=date(2026, 10, 10),
        data_termino=date(2026, 10, 15),
        cliente_nome="João Silva",
        veiculo=carro1,
        nome_condutor="Carlos Andrade",
        cnh_condutor="12345678900"
    )

    print(contrato.resumo_contrato())