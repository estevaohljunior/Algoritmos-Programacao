n1 = int(input())
n2 = int(input())
n3 = int(input())
media = (n1+n2+n3)/3
if media <0:
    print("Media invalida")
if media >= 70 and media <= 100:
    print("A media do aluno foi %.2f e ele foi APROVADO" %media)
elif media >= 40 and media < 70:
    print("A media do aluno foi %.2f e ele foi FINAL" %media)
elif media >= 0 and media <40:
    print("A media do aluno foi %.2f e ele foi REPROVADO" %media)
