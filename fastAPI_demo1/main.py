from fastapi import FastAPI
from Pessoa import ListaPessoas, Pessoa2, Aluno
import sqlite3

app = FastAPI()





"""

"""

@app.get("/setup")
async def setup_database():
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute("""
    Create Table alunos(
        id INTEGER primary key,
        nome TEXT,
        numero INTEGER,
        email TEXT
    )
    """)


    conn.close()


@app.get("/")
async def root():
    return {"message": "Hello World222"}

#http://127.0.0.1:8000/teste
@app.get("/teste")
async def rootTeste():
    p = ListaPessoas[0]
    return {"nome": f"{p.nome}", "idade": p.idade }

@app.get("/pessoas")
async def rootTeste():
    msg = []
    for p in ListaPessoas:
        msg.append({"nome": f"{p.nome}", "idade": p.idade })

    return msg

#http://127.0.0.1:8000/pessoa/5
@app.get("/pessoa/{id}")
async def list_pessoa_od(id: int):
    try:
        p = ListaPessoas[id]
        return {"nome": f"{p.nome}", "idade": p.idade}
    except:
        return {"Erro": f"a pessoa {id} não existe"}



#          /hello/Goncalo/2023
@app.get("/hello/{name}/{ano}")
async def say_hello(name: str, ano: int):
    msg = {"message": f"Hello {name}", "ano": ano}
    for i in range(10):
        msg[f"Mensagem {i}"] = f"conteudo da msg {i}: {i}"

    return msg

##Query Parameters
# ?id=210
@app.get("/testeqp")
async def testeqp(id: int):
    return id



'''
JSON
get vs Post
intro BaseModel
'''

@app.post("/pessoa2")
async def get_pessoa2(p: Pessoa2):
    print(p)
    return p


@app.get("/pessoa3")
async def get_pessoa3():
    p = Pessoa2(nome="Gonçalo", idade=20)
    return p



@app.post("/addAluno")
async def add_aluno(al: Aluno):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    conn.execute(f"""
        insert into Alunos ("nome", "numero", "email") 
                    values ("{al.nome}", {al.num}, "{al.email}")
    """)

    conn.commit()

    conn.close()