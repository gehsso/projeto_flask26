
from regras import calcular_media, verificar_situacao
from apresentacao import mostrar_resultado

nome = input("Nome do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = calcular_media(nota1,nota2)

media = calcular_media(nota1,nota2)
situacao = verificar_situacao(media)
mostrar_resultado(nome,media,situacao)











"""
# problemas:
Tudo em um lugar só.
Não dá para testar a média sem digitar no teclado.
Se eu quiser usar isso em outro lugar, tenho que copiar tudo.


#Versão 2: Separado em 3 Camadas

projeto/
├── main.py              ← conversa com o usuário
├── regras.py            ← faz as contas (o cérebro)
└── apresentacao.py      ← mostra a mensagem



#regras.py — O Cérebro (faz as contas)

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

# Só faz contas. Não tem input, não tem print.






#2️ apresentacao.py — Quem Mostra na Tela   

def mostrar_resultado(nome, media, situacao):
    print(f"{nome} tirou média {media} e está {situacao}")

 
 
 
 
 
 # main.py — Quem Conversa com o Usuário e com as demais camadas
 
 
from regras import calcular_media, verificar_situacao
from apresentacao import mostrar_resultado

nome = input("Nome do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)

mostrar_resultado(nome, media, situacao)







#Bônus: Agora dá para testar!

test_regras.py
from regras import calcular_media, verificar_situacao


def test_media():
    assert calcular_media(8, 6) == 7.0

def test_aprovado():
    assert verificar_situacao(7) == "Aprovado"

def test_reprovado():
    assert verificar_situacao(5) == "Reprovado"
    



Cada arquivo responde uma pergunta:
regras.py → "Como eu calculo?"
apresentacao.py → "Como eu mostro?"
main.py → "Quem chama tudo?"    





if nome.strip() == "":
    print("Erro: nome não pode ser vazio.")
    exit()

if not (0 <= nota1 <= 10):
    print(f"Erro: A nota deve estar entre 0 e 10.")
    exit()


if not (0 <= nota2 <= 10):
    print(f"Erro: A nota deve estar entre 0 e 10.")
    exit()
    
    
"""