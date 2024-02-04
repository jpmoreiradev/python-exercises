number = input('Digite o total de metros que você deseja converter: ')

if number.isdigit():
    metros = float(number)
    print(f'{metros} equivale a {metros * 100} Centimetros')
else:
    print('Por favor informe um numero na proxima vez')
