word = input('Digite o seu Gênero(M/F): ')


if(word.upper() == 'M'):
    print('M - Masculino')
elif(word.upper() == 'F'):
    print('F - Feminino')
else:
    print('Sexo Inválido.')
