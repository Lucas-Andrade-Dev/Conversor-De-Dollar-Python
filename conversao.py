# aqui vou criar um sistema que converta reais para dollar e dollar para reais

dolaremreal = 5.35

conversao = 0
print("Você quer converter Real ou Dollar?")

opcao = input("(1)Real (2)Dollar  ")

match opcao:
    case "1":
        valor = input("Digite a quantiade de Reais que deseja converter: R$ ")
        conversao = float(valor) / dolaremreal

        print(f'Voce converteu R${float(valor):,.2f} em ${conversao:,.2f}')

    case "2":
        valor = input("Digite a quantiade de Dollar que deseja converter: $ ")
        conversao = float(valor) * dolaremreal

        print(f'Voce converteu ${float(valor):,.2f} em R${conversao:,.2f}')
