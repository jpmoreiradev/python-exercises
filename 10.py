grade1 = float(input('Digite a Primeira nota: '))
grade2 = float(input('Digite a Segunda nota: '))

average = (grade1 + grade2) / 2

if average == 10:
    print('Aprovado com Distinção')
elif average >= 7:
    print('Aprovado')
else:
    print('REPROVADO')

print(f'Média: {average}')
