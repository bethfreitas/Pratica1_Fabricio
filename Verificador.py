def verificar(expressao):
    pilha = []
    pares = {'(': ')', '[': ']', '{': '}'}
    for i in expressao:
        if i in pares:
            pilha.append(i)
        elif i in pares.values():
            if not pilha or pares[pilha.pop()] != i:
                return False
    return len(pilha) == 0
#testando a função
expressao = ["(a+{*c)","(a+[b*c]-{d/e})","([]})","{[()]}"]
for exp in expressao:
    resultado = "válido " if verificar(exp) else "inválido"
    print(f"Expressão {exp} é {resultado}")


