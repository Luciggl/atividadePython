lojas=[];
listadeNomes=[];
vendedores = 0;
for i in range(5):
    nomeLoja = str(input("nome da loja: "));
    Produto = str.lower(input("Produto vendido: "));
    quantidadeVendedor = int(input("Quantidade de vendedores da loja: "));
    DadosLoja = [nomeLoja, Produto, quantidadeVendedor]
    lojas.append(DadosLoja)
    if(Produto == "perfume"):
        if(quantidadeVendedor >= 8):
            listadeNomes = [nomeLoja]
    elif(Produto == "roupas"):
        vendedores += quantidadeVendedor;
print("lojas que vendem perfume e têm mais de 8 funcionarios: ");
print(listadeNomes);
print("quantidade total de funcionários das lojas de roupas:");
print(vendedores);
print("fim do programa!!");