salario = float(input())
horas_extras = int(input())
extra = (salario / 44) * horas_extras
adicional = 0.1 * extra
salariofinal= salario + extra + adicional
print("%.2f"% salariofinal)
