def tokenizar(expressao):
    tokens = expressao.split() # quebra por espaços 
    pares = {
        '=':'Atribuiçao',
        '+':'Operador',''
        ';':'Fim de instrução',
    }
    for token in tokens: # type: ignore
        if token in pares: # type: ignore
            tipo = pares[token]  # type: ignore
        elif token.isnumeric():
            tipo = 'Número'
        else:
            tipo = 'Identificador'
        print(f"{token} -> {tipo}")
# testando
tokenizar("soma = 10 + 20 ;")
    

