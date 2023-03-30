num = int(input())
if (num == 1):
    print("Nordeste")
else:
    if (num == 2):
        print("Norte")
    else:
        if (num == 3 or num == 4):
            print("Centro-Oeste")
        else:
            if (num == 5 or num <= 9):
                print("Sul")
            else:
                if (num >= 10 or num <= 15):
                    print("Sudeste")

