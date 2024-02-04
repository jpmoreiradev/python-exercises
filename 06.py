number1 = input('Digite o primeiro número: ')
number2 = input('Digite o segundo número: ')



if number1.isdigit() and number2.isdigit(): 
    if float(number1) > float(number2):
        print("o maior numero é o primeiro", number1)
    elif float(number2) > float(number1):
        print("o maior numero é o segundo", number2)
    else:
        print("Numeros iguais")
else: 
    print('Por favor informe um numero na proxima vez')