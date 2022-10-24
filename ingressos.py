arquibancada = 100.00
cadeira = 200.00
vip = 350.00
taxa = 0.05
meia = 0.50
inteira = 1
print("digite o setor: (Arquibancada, Cadeira ou Vip)")
Setor = str.lower(input("=>"))
if(Setor == "arquibancada"):
    print("digite o tipo de entrada: (inteira ou meia)")
    Entrada = str.lower(input("=>"))
    if(Entrada == "inteira"):
        valorTotal = (arquibancada + (arquibancada * taxa))
        print(valorTotal)
    elif(Entrada == "meia"):
        valorTotal = ((meia * arquibancada) + (arquibancada * taxa))
        print(valorTotal)
    else:
        print("tipo de ingresso inválido")
elif(Setor == "cadeira"):
    print("digite o tipo de entrada: (inteira ou meia)")
    Entrada = str.lower(input("=>"))
    if(Entrada == "inteira"):
        valorTotal = (cadeira + (cadeira * taxa))
        print(valorTotal)
    elif(Entrada == "meia"):
        valorTotal = ((meia * cadeira) + (cadeira * taxa))
        print(valorTotal)
    else:
        print("tipo de ingresso inválido")
elif(Setor == "vip"):
    print("digite o tipo de entrada: (inteira ou meia)")
    Entrada = str.lower(input("=>"))
    if(Entrada == "inteira"):
        valorTotal =( vip + (vip * taxa))
        print(valorTotal)
    else:
        print("tipo de ingresso inválido")
else:
    print("Setor inválido")


