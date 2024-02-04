word = input('Digite uma letra: ')

letter = word.lower();

if(len(word) > 1):
    print(f'por favor digite somente uma letra')
elif(word.isdigit()):
    print(f'por favor digite uma letra')
elif(letter == 'a'):
    print(f'O {word} que foi digitado é VOGAL!')
elif(letter == 'e'):
    print(f'O {word} que foi digitado é VOGAL!')
elif(letter == 'i'):
    print(f'O {word} que foi digitado é VOGAL!')
elif(letter == 'o'):
    print(f'O {word} que foi digitado é VOGAL!')
elif(letter == 'u'):
    print(f'O {word} que foi digitado é VOGAL!')
else:
    print(f'O {word} que foi digitado é CONSOANTE!')


