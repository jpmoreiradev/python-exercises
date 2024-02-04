def soma(number1, number2):
    if(number1.isdigit() and number2.isdigit()): 
        soma = int(number1) + int(number2)
        return soma
    
    return False

number1 = input('Digite o primeiro número: ')
number2 = input('Digite o segundo número: ')

if soma(number1, number2):
    print("A soma é:", soma(number1, number2))
else:
    print("número Invalido.")