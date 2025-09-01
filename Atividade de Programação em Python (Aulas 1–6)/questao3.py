# Mensagem inicial
print("Oi, tudo bem? Bem vindo ao sistema da fábrica NJM - Natan Jose Maria!")

# Explicação dos modelos (menu)
print('\nModelos disponíveis:')
print('MCS - Camiseta Manga Curta Simples')
print('MLS - Camiseta Manga Longa Simples')
print('MCE - Camiseta Manga Curta com Estampa')
print('MLE - Camiseta Manga Longa com Estampa')
print('---------------------------------------------------\n')

# função pra escolher o modelo
def escolha_modelo():
    while True:
        modelo = input("Qual modelo você quer? (MCS/MLS/MCE/MLE): ")
        modelo = modelo.upper()

        if modelo == "MCS":
            return 1.80
        if modelo == "MLS":
            return 2.10
        if modelo == "MCE":
            return 2.90
        if modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido, tente novamente.")

# função pra perguntar quantidade de camisetas e aplicar desconto
def num_camisetas():
    while True:
        try:
            qtd = int(input("Quantas camisetas você deseja? "))

            if qtd > 20000:
                print("Uau! Esse número é alto demais. Para pedidos acima de 20.000 unidades, entre em contato com o nosso setor comercial.")
                print("Tente novamente.")
                continue

            if qtd < 20:
                return qtd
            if qtd >= 20 and qtd < 200:
                return qtd * 0.95
            if qtd >= 200 and qtd < 2000:
                return qtd * 0.93
            if qtd >= 2000 and qtd <= 20000:
                return qtd * 0.88

        except:
            print("Por favor insira numeros. Tente novamente.")

# função do frete
def frete():
    while True:
        print("\nEscolhe o frete:")
        print("0 = Retirar na fábrica (grátis)")
        print("1 = Transportadora (R$ 100)")
        print("2 = Sedex (R$ 200)")
        tipo = input("Digite a opção de frete (0/1/2): ")

        if tipo == "0":
            return 0
        elif tipo == "1":
            return 100
        elif tipo == "2":
            return 200
        else:
            print("Opção errada, digita 0, 1 ou 2.")

# parte principal do código
modelo_valor = escolha_modelo()
qtd_camiseta = num_camisetas()
valor_frete = frete()

# faz o total
total = (modelo_valor * qtd_camiseta) + valor_frete

# mostra resultado
print("\nResumo do pedido:")
print("Valor unitário do modelo escolhido: R$", round(modelo_valor, 2))
print("Quantidade com desconto aplicada:", round(qtd_camiseta))
print("Frete: R$", valor_frete)
print("Total a pagar: R$", round(total, 2))
