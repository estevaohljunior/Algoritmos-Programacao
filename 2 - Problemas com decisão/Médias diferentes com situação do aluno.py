tipo = input()
#n1 = int(input())
#n2 = int(input())
#n3 = int(input())


if tipo == "a":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    media_arit = (n1 + n2 + n3) / 3

    if media_arit >= 70 and media_arit <= 100:
        print("%.2f" % media_arit)
        print("Aprovado")
    elif media_arit >= 0 and media_arit <= 40:
        print("%.2f" % media_arit)
        print("Reprovado")
    elif media_arit >= 40 and media_arit <= 70:
        print("%.2f" % media_arit)
        print("Final")

elif tipo == "p":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())

    media_pondera = ((p1 * n1) + (p2 * n2) + (p3 * n3)) / (p1 + p2 + p3)
   # print("%.2f" % media_pondera)
    if media_pondera >= 70 and media_pondera <= 100:
        print("%.2f" % media_pondera)
        print("Aprovado")
    elif media_pondera >= 0 and media_pondera <= 40:
        print("%.2f" % media_pondera)
        print("Reprovado")
    elif media_pondera >= 40 and media_pondera <= 70:
        print("%.2f" % media_pondera)
        print("Final")


elif tipo == "h":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    media_harmo = 3 / (1 / n1 + 1 / n2 + 1 / n3)
    if media_harmo >= 70 and media_harmo <= 100:
        print("%.2f" % media_harmo)
        print("Aprovado")
    elif media_harmo >= 0 and media_harmo <= 40:
        print("%.2f" % media_harmo)
        print("Reprovado")
    elif media_harmo >= 40 and media_harmo <= 70:
        print("%.2f" % media_harmo)
        print("Final")


else:
    print("Escolha um tipo de media valida.")

