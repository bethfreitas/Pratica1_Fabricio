largura = int(input("Digite a largura do retangulo (maximo 20) "))
altura = int(input("Digite a altura do retangulo (maximo 20) "))
if altura > 20:
    print("Valor invalido")
else :
    for i in range (altura):
        print("*" * largura)
