from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# aredonda pra cima
print('A raiz fr {} é igual a {}'.format(num, math.ceil(raiz)))
# aredonda para baixo
print('A raiz de {} é igual a{}'.format(num, math.floor(raiz)))
