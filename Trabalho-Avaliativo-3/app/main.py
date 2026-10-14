from app.routers import autores, livros
from fastapi import FastAPI

app = FastAPI(
    title="API Sistema de Biblioteca",
    version="1.0.0",
    description=(
        "API desenvolvida para a Disciplina de Arquitetura de Software"
    ),
)

app.include_router(autores.router)
app.include_router(livros.router)


@app.get("/")
def root():
  return {"message": "API da Biblioteca rodando com sucesso! Acesse /docs"}