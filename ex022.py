nome = str(input('Digite seu nome completo: '))
tamanho = (len(nome) - nome.count(' '))
alta = nome.upper()
baixa = nome.lower()
dividido = nome.split()
print("""O seu nome tem {} letras
      Escrito em maiúsculas é assim: {}
      Escrito em minúsculas é assim: {}
      Seu primeiro nome é {} e ele tem {} letras.""".format(tamanho, alta, baixa, dividido[0], len(dividido[0])))