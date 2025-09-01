# Mensagem de boas-vindas com meu nome e sobrenome
print('Seja bem-Vindo Natan Jose Maria');

# Solicitação de valor do pedido ao usuário
valor_pedido = float(input('Insira o Valor do Pedido: R$'));

# Solicitação de quantidade de parcelas ao usuário
quantidade_parcelas = float(input('Insira a quatidade de parcelas: '));

# Listagem de Juros conforme quatidade de parcelas
# Se for menor que 4 = 0% de juros
if quantidade_parcelas < 4:
    juros = 0 / 100  # 0%

# Se for maior ou igual a 4 e menor que 6 = 4% de juros (4/100)
elif quantidade_parcelas < 6:
    juros = 4 / 100  # 4%

# Se for maior ou igual a 6 e menor que 9 = 8% de juros (8/100)
elif quantidade_parcelas < 9:
    juros = 8 / 100  # 8%

# Se for maior ou igual a 9 e menor que 13 = 16% de juros (16/100)
elif quantidade_parcelas < 13:
    juros = 16 / 100  # 16%

# Se for maior ou igual a 13 = 32% de juros (32/100)
else:
    juros = 32 / 100  # 32%

 # Cálculo do valor de cada parcela
valorDaParcela = (valor_pedido * (1 + juros)) / quantidade_parcelas

# Cálculo total com juros
valorTotalParcelado = valorDaParcela * quantidade_parcelas

# Resultado final
print(f"Valor da parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total com juros: R$ {valorTotalParcelado:.2f}")