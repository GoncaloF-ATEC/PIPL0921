from pydantic import BaseModel

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

ListaPessoas = [Pessoa("Joao", 30), Pessoa("Maria", 38)]



class Pessoa2(BaseModel):
    nome: str
    idade: int
