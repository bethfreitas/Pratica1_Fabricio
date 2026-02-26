def verificar_senha(senha):
    estado = 0
    for i in senha:
        match estado:
            case 0:
                if i == "1":
                    estado = 1
                else:
                    estado = 0
            case 1:
                if i == "2":
                    estado = 2
                else:
                    estado = 0
            case 2:
                if i == "3":
                    estado = 3
                else:
                    estado = 0
    if estado == 3:
        print(f"Acesso concedido")
    else:
        print(f"senha inválida")
senha = input("Digite a senha: ")
verificar_senha(senha)





