d = int(input('Por Quantos dias o senhor pretende alugar o carro ? '))
k = float(input('Quantos km você pretende percorrer ao todo ?'))
t = (k * 0.15) + (60 * d)
print (f'Nesse caso, alugando o carro durante {d} dias e percorrendo {k} KM, \no senhor pagará R${t} ao todo')
