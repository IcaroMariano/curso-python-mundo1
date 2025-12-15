velocidade = float(input('Digite a velocidade: '))
if velocidade > 80: 
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('VOcê deve pagar uma multa de R$ {:.2f}'.format(multa))
else:
    print('Tenha uma boa viagem!')