frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posiução {}'.format(frase.rfind('A') + 1))