name = input('Name: ')
password = input('Senha: ')

while name == password:
    print("senha não pode ser igual ao nome")
    name = input('Name: ')
    password = input('Senha: ')

print('usuario cadastrado com sucesso') 

