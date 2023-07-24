from fastapi import FastAPI
from Pessoa import ListaPessoas

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

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
@app.get("/testeqp")
async def testeqp(id: int):
    return id
