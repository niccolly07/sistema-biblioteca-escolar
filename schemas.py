from pydantic import BaseModel


class LivroSchema(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int


class LivroPublic(LivroSchema):
    id: int


class LivroDB(LivroSchema):
    id:int


class LivroList(BaseModel):
    livros: list[LivroPublic]


class Message(BaseModel):
    message: str
