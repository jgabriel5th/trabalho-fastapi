from typing import List
from app.core.database import get_db
from app.models.models import AutorModel, LivroModel
from app.schemas.schemas import LivroCreate, LivroResponse, LivroUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/livros", tags=["Livros"])

# Validação de integridade referencial: Garante que o livro 
# só será cadastrado se o autor correspondente realmente existir no banco.

@router.post(
    "/", response_model=LivroResponse, status_code=status.HTTP_201_CREATED
)
def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
  autor = (
      db.query(AutorModel).filter(AutorModel.id == livro.autor_id).first()
  )
  if not autor:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="O autor informado não existe.",
    )
  novo_livro = LivroModel(**livro.model_dump())
  db.add(novo_livro)
  db.commit()
  db.refresh(novo_livro)
  return novo_livro


@router.get("/", response_model=List[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
  return db.query(LivroModel).all()


@router.get("/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
  livro = db.query(LivroModel).filter(LivroModel.id == livro_id).first()
  if not livro:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado"
    )
  return livro


@router.delete("/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
  livro = db.query(LivroModel).filter(LivroModel.id == livro_id).first()
  if not livro:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado"
    )
  db.delete(livro)
  db.commit()
  return None
