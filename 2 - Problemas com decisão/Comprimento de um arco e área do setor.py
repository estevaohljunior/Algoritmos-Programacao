raio = float(input())
angulo = float(input())
pi = 3.14
comprimento = (angulo * pi * raio) / 180

#formatacao e arrendodamento round (v,2)

print( round (comprimento, 2) )
setor = (angulo * pi * raio * raio) / 360
print( round (setor, 2) )
