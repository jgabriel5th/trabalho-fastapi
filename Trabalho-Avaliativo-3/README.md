
```markdown
# API Sistema de Biblioteca - Arquitetura de Software

Trabalho Prático 03 desenvolvido para a disciplina de **Arquitetura de Software** (Bloco IV - UNINASSAU)[cite: 1].

---

## 📌 Descrição do Modelo de Negócio
A aplicação consiste em uma API RESTful desenvolvida em **FastAPI** para o gerenciamento de uma biblioteca digital. O sistema controla dois domínios principais:
- **Autores:** Escritores cadastrados no sistema.
- **Livros:** Obras literárias vinculadas obrigatoriamente a um autor através de uma chave estrangeira (`ForeignKey`).

---

## 🔗 Entidades e Relacionamento
- **Autor:** 
  - `id` (Chave Primária, Inteiro)
  - `nome` (Texto, Obrigatório)
  - `nacionalidade` (Texto, Opcional)
- **Livro:** 
  - `id` (Chave Primária, Inteiro)
  - `titulo` (Texto, Obrigatório)
  - `ano_publicacao` (Inteiro, Obrigatório)
  - `paginas` (Inteiro, Opcional)
  - `autor_id` (Chave Estrangeira apontando para `autores.id`)
- **Relacionamento:** Um autor pode possuir múltiplos livros (relação de 1 para N implementada via `relationship` e `back_populates` do SQLAlchemy)[cite: 1].

---

## ⚙️ Instruções de Instalação e Execução (Passo a Passo)

Para clonar e rodar este projeto na sua máquina, siga os passos abaixo no terminal:

### 1. Clonar o Repositório
```bash
git clone [https://github.com/franciscocoelho-dev/arquitetura.git](https://github.com/franciscocoelho-dev/arquitetura.git)
cd arquitetura

```

### 2. Criar e Ativar o Ambiente Virtual

O ambiente virtual isola as dependências do projeto no seu computador:

* **No Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate

```


* **No Windows (Prompt de Comando ou PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate

```



*(Nota: Você saberá que deu certo quando aparecer `(venv)` no início da linha do terminal).*

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale os pacotes necessários (FastAPI, Uvicorn, SQLAlchemy, Alembic, Pydantic):

```bash
pip install -r requirements.txt

```

### 4. Executar as Migrações do Banco de Dados

O banco de dados SQLite local (`database.db`) será criado automaticamente através das migrações versionadas pelo Alembic:

```bash
alembic upgrade head

```

### 5. Iniciar a Aplicação

Com o banco pronto, inicie o servidor local do FastAPI com recarga automática:

```bash
uvicorn app.main:app --reload

```

### 6. Acessar a Documentação

Abra o seu navegador e acesse a interface interativa do Swagger para testar todos os recursos:
👉 **`http://127.0.0.1:8000/docs`**

---

## 📍 Lista de Endpoints Implementados

### **Autores**

* `POST /autores/` - Cadastra um novo autor


* `GET /autores/` - Lista todos os autores cadastrados


* `GET /autores/{id}` - Consulta um autor específico por ID


* `PUT /autores/{id}` - Atualiza os dados de um autor


* `DELETE /autores/{id}` - Remove um autor do sistema



### **Livros**

* `POST /livros/` - Cadastra um novo livro (realiza a **validação de integridade** para garantir que o `autor_id` informado realmente existe no banco)


* `GET /livros/` - Lista todos os livros cadastrados


* `GET /livros/{id}` - Consulta um livro específico por ID


* `DELETE /livros/{id}` - Remove um livro do sistema