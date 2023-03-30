diaria = int(input("Digite a quantidade de dias de locacao:\n"))
km = int(input("Digite a quantidade de km rodados:\n"))

total = (30*diaria)+(0.01*km)
total = total -(total*0.1)
print("Valor a pagar pelo aluguel: R$", "%.6f"%total)
