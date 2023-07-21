
class Pessoa:
     def __init__(self, nome: str, idade: int, email: str):
          self.nome = nome
          self.idade = idade
          self.email = email

     def __str__(self):
          return f"Pessoa(nome:{self.nome}, idade:{self.idade}, email: {self.email})"

class Aluno(Pessoa):
     def __init__(self, nome: str, idade: int, email: str, turma:str):
          Pessoa.__init__(nome, idade, email)
          self.turma = turma

     def __str__(self):
          return f"{Pessoa.__str__()}, turma: {self.turma}"
