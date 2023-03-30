p1=input("Telefonou para a vitima?\n")
p2=input("Esteve no local do crime?\n")
p3=input("Mora perto da vitima?\n")
p4=input("Devia para a vitima?\n")
p5=input("Ja trabalhou com a vitima?\n")
cont=0

if p1=="True":
    cont=cont+1

if p2=="True":
    cont=cont+1

if p3=="True":
    cont=cont+1

if p4=="True":
    cont=cont+1

if p5=="True":
    cont=cont+1

if cont==3:
    print("Cumplice")
if cont==4:
    print("Cumplice")
if cont==5:
    print("Assassino")
if cont==2:
    print("Suspeita")
if cont==0:
    print("Inocente")
if cont==1:
    print("Inocente")
    
