stop = False

while stop == False:
  number = input('Digite um numero de 0 a 10: ')
  if(number.isdigit() and int(number) >= 0 and int(number) <= 10):
    print(number)
    stop = True
