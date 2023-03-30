num1 = int(input())
num2 = int(input())
soma = 0

if num1 > num2:
    for c in range(num2, num1 + 1):
        if c > 0:
            soma = soma + c
if num1 < num2 :
    for n in range(num1, num2 + 1):  #Com o + 1 at� o extremo, ou seja, o �ltimo algarismo.
        if n > 0:
            soma += n
print(soma)
