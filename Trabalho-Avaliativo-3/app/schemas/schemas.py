from typing import Optional
from pydantic import BaseModel


class AutorCreate(BaseModel):
  """Schema base contendo os atributos comuns para Autores."""
  nome: str
  nacionalidade: Optional[str] = None


class AutorUpdate(BaseModel):
  nome: Optional[str] = None
  nacionalidade: Optional[str] = None


class AutorResponse(BaseModel):
  id: int
  nome: str
  nacionalidade: Optional[str] = None

  class Config:
    from_attributes = True


class LivroCreate(BaseModel):
  """Schema base contendo os atributos essenciais para Livros."""
  titulo: str
  ano_publicacao: int
  paginas: Optional[int] = None
  autor_id: int


class LivroUpdate(BaseModel):
  titulo: Optional[str] = None
  ano_publicacao: Optional[int] = None
  paginas: Optional[int] = None


class LivroResponse(BaseModel):
  id: int
  titulo: str
  ano_publicacao: int
  paginas: Optional[int] = None
  autor_id: int

  class Config:
    from_attributes = True