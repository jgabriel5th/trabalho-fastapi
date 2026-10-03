# Trabalho Prático 02 - Arquitetura de Software

**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Arquitetura de Software

---

## 1. Identificação de Classes
- Pessoa (Abstrata), PessoaFisica, PessoaJuridica
- Veiculo (Abstrata), Carro, Moto, Caminhao
- ContratoLocacao, Condutor, Manutencao

---

## 2. Atributos e Métodos
### `Pessoa`
- **Atributos:** `nome_ou_razao_social`, `documento`, `telefone`
- **Métodos:** `validar_documento()`, `atualizar_contato()`

### `PessoaFisica`
- **Atributos:** `cpf`, `rg`, `data_nascimento`
- **Métodos:** `validar_cpf()`, `obter_idade()`

### `PessoaJuridica`
- **Atributos:** `cnpj`, `inscricao_estadual`, `nome_fantasia`
- **Métodos:** `validar_cnpj()`, `emitir_nota_fiscal()`

### `Veiculo`
- **Atributos:** `placa`, `modelo`, `ano`, `valor_diaria`
- **Métodos:** `calcular_aluguel()`, `alterar_status_disponibilidade()`

### `Carro`
- **Atributos:** `quantidade_portas`, `possui_ar_condicionado`, `tipo_combustivel`
- **Métodos:** `verificar_ar_condicionado()`, `exibir_especificacoes()`

### `Moto`
- **Atributos:** `cilindradas`, `tipo_partida`, `possui_abs`
- **Métodos:** `verificar_capacidade_tanque()`, `exibir_especificacoes()`

### `Caminhao`
- **Atributos:** `capacidade_carga_toneladas`, `numero_eixos`, `tipo_carroceria`
- **Métodos:** `verificar_limite_carga()`, `exibir_especificacoes()`

### `ContratoLocacao`
- **Atributos:** `data_inicio`, `data_termino_prevista`, `valor_total`, `status`
- **Métodos:** `calcular_valor_total()`, `encerrar_contrato()`

### `Condutor`
- **Atributos:** `nome`, `numero_cnh`, `categoria_cnh`
- **Métodos:** `validar_cnh()`, `exibir_dados_condutor()`

### `Manutencao`
- **Atributos:** `data`, `tipo_servico`, `custo`
- **Métodos:** `registrar_manutencao()`, `obter_resumo_servico()`

---

## 3. Herança
- **Veiculo -> Carro, Moto, Caminhao:** Partilham atributos básicos (placa, modelo) e especializam características próprias.
- **Pessoa -> PessoaFisica, PessoaJuridica:** Partilham dados de contacto e especializam o tipo de documento (CPF ou CNPJ).

---

## 4. Relacionamentos entre Classes
- **ContratoLocacao - Condutor (Composição):** O condutor só existe atrelado ao contrato.
- **Veiculo - Manutencao (Composição):** A manutenção faz parte do histórico do veículo.
- **ContratoLocacao - Veiculo (Agregação):** O veículo existe independentemente do contrato.
- **ContratoLocacao - Pessoa (Agregação):** O cliente existe independentemente do contrato.

---

## 5. Implementação Parcial em Python
A implementação do código encontra-se no ficheiro `sistema_locadora.py`.