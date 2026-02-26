altura = int(input("Digite a altura do triangulo (maximo 20) "))
if altura > 20:
    print("Valor invalido")
else :
    for i in range( altura +1):
        print("*" * i)