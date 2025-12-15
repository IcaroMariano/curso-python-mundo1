from random import randint
from time import sleep
computador = randint(0, 5)
print("-=-" * 20)
print("Tente adivinhar o número entre 1 e 5. ")
print("-=-" * 20)
jogador = int(input("Digite um número entre 1 e 5. "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("Parabéns, você venceu!")
else:
    print("Você perdeu! O número correto era {} e você digitou {}". format(computador, jogador))