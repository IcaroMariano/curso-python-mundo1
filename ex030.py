n = int(input('Digite um número: '))
res = n % 2
if res == 0:
    print('O número {} é um número par'.format(n))
else:
    print('O número {} é um número ímpar'.format(n))