
from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import LivroDB, LivroList, LivroPublic, LivroSchema, Message

app = FastAPI()

# Lista que simula o banco de dados
database = {}


@app.get("/")
def read_root():
    return {"message": "Olá Mundo!"}


@app.post(
    "/livros/",
    status_code=HTTPStatus.CREATED,
    response_model=LivroPublic,
)
def create_livro(livro: LivroSchema):
    livro_id = max(database.keys(), default=0) + 1

    livro_com_id = LivroDB(**livro.model_dump(), id=livro_id)

    database[livro_id] = livro_com_id

    return livro_com_id


@app.get("/livros/", response_model=LivroList)
def read_livros():
    return {"livros": list(database.values())}


@app.put("/livros/{livro_id}", response_model=LivroPublic)
def update_livro(livro_id: int, livro: LivroSchema):
    if livro_id not in database:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Livro não encontrado",
        )

    livro_atualizado = LivroDB(**livro.model_dump(), id=livro_id)

    database[livro_id] = livro_atualizado

    return livro_atualizado


@app.delete("/livros/{livro_id}", response_model=Message)
def delete_livro(livro_id: int):
    if livro_id not in database:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Livro não encontrado",
        )

    del database[livro_id]

    return {"message": "Livro excluído com sucesso"}
