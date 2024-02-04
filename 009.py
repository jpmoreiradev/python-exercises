word = input('Digite uma letra: ').lower()

if(len(word) > 1):
    print(f'por favor digite somente uma letra')
elif(word.isdigit()):
    print(f'por favor digite uma letra')
elif word in 'aeiou':
    print(f'A letra {word} é uma vogal.')
else:
    print(f'A letra {word} é uma consoante.')
     



