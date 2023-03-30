ano_dose1 = int(input()) # Ano em que tomou s primeira dose

intervalo = int(input()) # Intervalo que deve ser atribuido por entrada

ano = ano_dose1  # Aqui foi criado uma variavel para somar com o intervalo para dar o resultado de quantos em quantos anos tomara a proxima dose

for i in range(3):

  ano = ano + intervalo
  
  print('{} '.format(ano), end = '') # O Comando end = '' serve para n�o pular de linha
  
