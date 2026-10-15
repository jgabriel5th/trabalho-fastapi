from typing import List
from app.core.database import get_db
from app.models.models import AutorModel
from app.schemas.schemas import AutorCreate, AutorResponse, AutorUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post(
    "/", response_model=AutorResponse, status_code=status.HTTP_201_CREATED
)
def criar_autor(autor: AutorCreate, db: Session = Depends(get_db)):
  """
    Endpoint responsável por cadastrar um novo autor no banco de dados.
    Realiza validação dos campos obrigatórios e persiste a entidade.
    """
  novo_autor = AutorModel(**autor.model_dump())
  db.add(novo_autor)
  db.commit()
  db.refresh(novo_autor)
  return novo_autor


@router.get("/", response_model=List[AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
  return db.query(AutorModel).all()


@router.get("/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int, db: Session = Depends(get_db)):
  autor = db.query(AutorModel).filter(AutorModel.id == autor_id).first()
  if not autor:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Autor não encontrado"
    )
  return autor


@router.put("/{autor_id}", response_model=AutorResponse)
def atualizar_autor(
    autor_id: int, autor_data: AutorUpdate, db: Session = Depends(get_db)
):
  autor = db.query(AutorModel).filter(AutorModel.id == autor_id).first()
  if not autor:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Autor não encontrado"
    )
  for key, value in autor_data.model_dump(exclude_unset=True).items():
    setattr(autor, key, value)
  db.commit()
  db.refresh(autor)
  return autor


@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_autor(autor_id: int, db: Session = Depends(get_db)):
  autor = db.query(AutorModel).filter(AutorModel.id == autor_id).first()
  if not autor:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Autor não encontrado"
    )
  db.delete(autor)
  db.commit()
  return None