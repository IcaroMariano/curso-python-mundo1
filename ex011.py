largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede: "))
area = largura * altura
print(f"A área da sua parede vale {area:.2f}m2")
tinta = area / 2
print(f"Para pintar sua parede, você precisará de {tinta}l de tinta")