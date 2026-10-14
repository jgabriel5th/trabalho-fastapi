from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class AutorModel(Base):
  __tablename__ = "autores"

  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String, nullable=False)
  nacionalidade = Column(String, nullable=True)

  livros = relationship(
      "LivroModel", back_populates="autor", cascade="all, delete-orphan"
  )


class LivroModel(Base):
  __tablename__ = "livros"

  id = Column(Integer, primary_key=True, index=True)
  titulo = Column(String, index=True, nullable=False)
  ano_publicacao = Column(Integer, nullable=False)
  paginas = Column(Integer, nullable=True)
  autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)

  autor = relationship("AutorModel", back_populates="livros")