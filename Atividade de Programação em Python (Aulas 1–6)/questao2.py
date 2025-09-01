# Exibe nome e cardápio
print("----- Bem-vindo à Loja de Marmitas do Natan José Maria -----")
print("----------------------------- Cardápio -----------------------------")
print("|  Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |")
print("|    P     |      R$ 16.00       |      R$ 15.00        |")
print("|    M     |      R$ 18.00       |      R$ 17.00        |")
print("|    G     |      R$ 22.00       |      R$ 21.00        |")

# Acumulador de valor total
valor_total = 0

# Loop principal do programa
while True:
# Escolha do cardapio
    sabor = input("Entre com o sabor desejado (BA/FF): ").upper()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        continue  # volta ao início do loop

# Escolha do tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue  # volta ao início do loop

    # Verificação do preço
    if sabor == "BA":
        if tamanho == "P":
            preco = 16.00
        elif tamanho == "M":
            preco = 18.00
        else:
            preco = 22.00
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15.00
        elif tamanho == "M":
            preco = 17.00
        else:
            preco = 21.00

 # Mostra o item escolhido e acumular o valor
    print(f"Você pediu um {'Bife Acebolado' if sabor == 'BA' else 'Filé de Frango'} no tamanho {tamanho}: R$ {preco:.2f}")
    valor_total += preco

# Pergunta se deseja continuar
    mais = input("Deseja mais alguma coisa? (S/N): ").upper()
    if mais == "N":
        break
    elif mais != "S":
        print("Opção inválida. Encerrando o pedido.")
        break

# Total final
print(f"\nO valor total a ser pago: R$ {valor_total:.2f}")