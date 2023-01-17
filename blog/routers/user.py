from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter()
get_db = database.get_db


@router.post('/users/', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(
        name=request.name, email=request.email, password=Hash.brypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}", response_model=schemas.ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id  {id} is not available')
    return user
