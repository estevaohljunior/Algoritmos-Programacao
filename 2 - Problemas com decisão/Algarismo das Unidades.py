num = int(input())
if (num < 0):
    num = num * (-1)
    u = num // 1 % 10 * (-1)
    print("Digite um numero:")
    print("Algarismo das unidades: {}" . format(u))
else:
    u = num // 1 % 10
    print("Digite um numero:")
    print("Algarismo das unidades: {}" . format (u))
