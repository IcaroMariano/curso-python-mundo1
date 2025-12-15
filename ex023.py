num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Analisando o número {}...
      a unidade é {}
      a dezena {}
      a centena é {}
      o milhar é {}. """. format(num, u, d, c, m))