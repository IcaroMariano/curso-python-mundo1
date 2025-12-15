print("-=" * 12)
print("Analisador de Triângulos")
print("=-" * 12)
r1 = float(input("Digite o primeiro seguimento: "))
r2 = float(input("Digite o segundo seguimento: "))
r3 = float(input("Digite o terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima podem formar um Triângulo!")
else:
    print("Os seguimentos acima NÃO PODEM formar um triângulo!")