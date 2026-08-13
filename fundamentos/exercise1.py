"""
Escreva um programa que:
Leia o nome de três produtos e seus respectivos preços.
Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).

Imprima:

O dicionário completo.
O produto mais caro.
A média dos preços.

Exemplo
Entrada:

Arroz
15.50

Feijão
8.90

Macarrão
6.75

Saída:

{'Arroz': 15.5, 'Feijão': 8.9, 'Macarrão': 6.75}
Arroz
10.38
"""
product1Name    = input("Digite o nome do produto 1:\n")
product1Price   = float(input("Digite o valor do produto 1:\n"))

product2Name    = input("Digite o nome do produto 2:\n")
product2Price   = float(input("Digite o valor do produto 2:\n"))

product3Name    = input("Digite o nome do produto 3:\n")
product3Price   = float(input("Digite o valor do produto 3:\n"))

products = {
    product1Name : product1Price,
    product2Name : product2Price,
    product3Name : product3Price,
}

print(products)

biggerPrice     = product1Price
biggerPriceName = product1Name

average = (product1Price + product2Price + product3Price)/3

if biggerPrice < product2Price:
    biggerPrice     = product2Price
    biggerPriceName = product2Name
if biggerPrice < product3Price:
    biggerPrice     = product3Price
    biggerPriceName = product3Name
 
print(biggerPriceName)
print(f"{average:.2f}")