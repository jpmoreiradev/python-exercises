name = input('Name: ')
age = int(input('Idade: '))
saler = float(input('Salário: '))
sex = input('Sexo(f/m): ')
stats = input('Estado Civil(s/c/v/d): ')

if (len(name) > 3 and age > 0 and age < 150 and saler > 0 and sex.lower() in 'fm' and stats.lower() in 'scvd'):
    print('usuario cadastrado com sucesso.') 
elif (len(name) <= 3):
    print('o nome do cliente tem que ser maior que 3.')
elif (age < 0 or age > 150):
    print('a idade do cliente é inválida.')   
elif (saler < 0): 
    print('Salario inválido.')
elif (sex.lower() != 'f' and sex.lower() != 'm'):
    print('Sexo inválido por favor digite m ou f.')
elif (stats.lower() != 's' and stats.lower() != 'c' and stats.lower() != 'v' and stats.lower() != 'd'):
    print('Estado Civil inválido por favor figite s para solteiro, c para casado, v para viúvo, e d para divóciado.')
else: 
    print('algo deu errado tente novamente mais tarde')








