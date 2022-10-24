Contador = 0
Dicionario = {}

while Contador < 10:
    login = input("digite o login: ")
    senha = input("digite a senha: ")
    if login in Dicionario:
        print("login ja existe")
    elif len(senha) < 6:
        print("Senha muiro curta")
    else:
        Dicionario[login] = senha
        Contador += 1
        print("login cadastrado com sucesso")

