tamanho = int(input("Digite o tamanho(maximo 20) "))
if tamanho > 20:
    print("Valor invalido")
else:
    for i in range(tamanho):
        espaços = " " * i
        print(espaços + "*" * (tamanho - i))