# Desconto no produto
n1 = float(input('Qual o valor do produto que deseha, senhor ? '))
desconto = n1 * 5 / 100
vista = n1 - (n1 * 5/100)
print(f'Somente hoje, caso o senhor pague à vista,\nreceberá 5% de desconto, o que equivale a R${desconto:.2f} \ne sua compra sairá por R$ {vista:.2f}')
