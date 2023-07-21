from fastapi import FastAPI
from  Pessoa import ListaPessoas

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


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

#          /hello/Goncalo/2023
@app.get("/hello/{name}/{ano}")
async def say_hello(name: str, ano: int):
    msg = {"message": f"Hello {name}", "ano": ano}
    for i in range(10):
        msg[f"Mensagem {i}"] = f"conteudo da msg {i}: {i}"

    return msg



