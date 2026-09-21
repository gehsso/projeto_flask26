def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >=4 :
        return "Exame Final"
    return "Reprovado"