viagem = float(input('Digite a distância da viagem: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('Para uma viagem de {}KM, o preço da passagem é de R${}'.format(viagem, preco))