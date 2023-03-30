r1 = float(input())
r2 = float (input())
pi = 3.14
Area = pi ** r1
Area2 = pi ** r2
if (Area == Area2):
    print("Iguais")
elif (Area > Area2):
    print("Primeiro circulo")
elif (Area2 > Area):
    print("Segundo circulo")
    
