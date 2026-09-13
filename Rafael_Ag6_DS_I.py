# Titulo do programa
print(f"\33[1m{'  Lojas Phenix  ':=^60}\33[0m")
print()

preco = float(input("Informe o valor das Compras: R$"))

# O bloco condicional define apenas a taxa de desconto e a mensagem de cada faixa
if preco < 200:
    taxa_desconto = 0.05
    mensagem = "Compras com valor inferior à R$200,00 o cliente tem desconto de 5%"
elif preco < 300:
    taxa_desconto = 0.10
    mensagem = "Compras com valor de R$200,00 ou até R$300,00 o cliente tem desconto de 10%"
else:
    taxa_desconto = 0.15
    mensagem = "Compras com valor de R$300,00 ou mais, o cliente tem desconto de 15%"

# Cálculo executado uma única vez
# O número 1 representa 100% do valor total (1.0).
# Ao subtrair a taxa, obtemos a fração decimal restante da compra (ex: 1 - 0.10 = 0.90).
novo_preco = preco * (1 - taxa_desconto)

print()
print(mensagem)
# Exibição executada uma única vez, desconto aplicado e valor final das compras
print(f"Desconto aplicado: R${preco * taxa_desconto:.2f}")
print(f"O valor das suas compras é de R${novo_preco:.2f}")
#Multiplicar a quebra de linha, permite definir a quantidade de espaço de forma visual
print("\n" * 2)   
#Mensagem final para encerramento do programa
print(f"\33[1m{'Obrigado por comprar na Lojas Phenix, volte sempre!':^60}\33[0m")