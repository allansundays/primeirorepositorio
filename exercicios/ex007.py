# Operações aritméticas
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
div_int = n1 // n2
exp = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.' .format(soma, multi, div), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(div_int, exp))
