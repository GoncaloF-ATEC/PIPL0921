notaAluno = 9.9


'''

< 10 -> aporvado

8 -  9.9 -> recup

< 8 -> não aprovado

'''

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