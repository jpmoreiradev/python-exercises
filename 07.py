number = input('Digite um numero: ')

if number.isdigit():
    if float(number) > 0: 
        print('Numero informado é POSITIVO')
    elif float(number) < 0:
        print('Numero informado é NEGATIVO')
    else:
        print("O numero é neutro")
else:
    print('Por favor informe um numero na proxima vez')