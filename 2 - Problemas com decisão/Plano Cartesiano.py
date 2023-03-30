x = float(input())
y = float(input())

if x == 0:
    if y == 0:
        print('Sobre a origem')
    if y != 0:
        print('Sobre o eixo y')
if y == 0:
    if x != 0:
        print('Sobre o eixo x')
if x > 0:
    if y > 0:
        print('Primeiro Quadrante')
    if y < 0:
        print('Quarto Quadrante')
if x < 0:
    if y > 0:
        print('Segundo Quadrante')
    if y < 0:
        print('Terceiro Quadrante')
        
