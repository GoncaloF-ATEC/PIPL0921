from fastapi import FastAPI

app = FastAPI()



#127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}


#127.0.0.1:8000/hello
@app.get("/hello")
async def root2():
    return {"message": "Hello World 3 "}


#127.0.0.1:8000/hello
@app.get("/hello/{name}")
async def say_hello2(name: str):
    return {"message": f"Hello {name}"}



@app.post("/add")
async def add_data(nome: str):
    return {"message": f"Hello {nome}"}