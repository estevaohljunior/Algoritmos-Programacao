num1 = int(input())
num2 = int(input())

for c in range(num1, num2 + 1): # O for ( VARI�VEL ) in range (assume o intervalo entre os n�meros).
    if c % 2 != 0:   # O num2 + 1 ir� incluir at� o ultimo n�mero desejado.
        print(c)
        
