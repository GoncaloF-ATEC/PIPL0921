
'''

notaAluno = 9.9




notaAluno = ("João", 10)
print(notaAluno[1])
lista_notas = [10, 1, 12, 14, 1, 20, 10, 7, 8]
lista_nomes = ["Joao", "maria", "Rita", "Ines", "mario", "rui", "luis", "pedro", "Hugo"]



list_av = [("Joao", 10),("maria", 11),("Rita", 9),("luis", 2),("paulo", 2),("Nuno", 10)]



def is_aprovado(nota, nome_aluno):
    if nota >= 10:
        print(f"{nome_aluno} foi aporvado com {nota} valor")
    elif nota >= 8:
        print(f"{nome_aluno} foi a Exame oral {nota} valor")
    else:
        print(f"{nome_aluno} foi não aprovado {nota} valor")

def isAprovadoV2(aluno):
    is_aprovado(aluno[1], aluno[0])


def add_nota(nota, aluno):
    new_aluno = (aluno, nota)
    list_av.append(new_aluno)


add_nota(20, "Ricardo")


list_size = lista_notas.__len__()

for i in range(list_size):
    is_aprovado(lista_notas[i], lista_nomes[i])


def teste(nome:str, idade:int = 10) -> (str, int):
    return f"{nome}, idade: {idade}"


print(teste("joao", 19))

valor = 100

while valor > 0:
    print(valor)
    valor += 1

'''

print("Sets")

my_set = {"valor1", "valor2", "valor3"}

for set_val in my_set:
    print(set_val)
print(len(my_set))
print("----v2----")
my_set.add("Joao")
print(len(my_set))
my_set.add("Joao")
print(len(my_set))
my_set.remove("Joao")
print(len(my_set))
#my_set.remove("maria")
for set_val in my_set:
    print(set_val)
my_set.add("Joao")
print(my_set.__contains__("Joao"))

def safe_remove(myset:set, valor):
    if myset.__contains__(valor):
        myset.remove(valor)
        return True
    else:
        return False


safe_remove(my_set, "retetre")

print("----v3----")
for set_val in my_set:
    print(set_val)

print("----Conjuntos----")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.intersection(y))

print(x.union(y))


print(x.difference(y))
print(x.symmetric_difference(y)) #x.union(y) - x.intersection(y)

print(x.union(y) - x.intersection(y))


print("----------dicts-------------")

alunos = {"nome": "Joao", "nota": 10, "escola": "Atec", "turma" : "PI"}
alunos2 = {"nome": "Joao2", "nota": 10, "escola": "Atec2", "turma" : "PI2"}

print(alunos["nome"])
print(alunos.get("nota"))
alunos["novoCampo"] = "Novo valor"

print(alunos)
alunos.popitem() # remove o ultima a ser adicionado
print(alunos)