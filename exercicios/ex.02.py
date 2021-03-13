#Dissecando variável
n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('só tem espaços?', n.isspace())
print('é um número?', n.isnumeric())
print('é uma palavra?', n.isalpha())
print('Possui letras e números?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('está capitalizada?', n.istitle())

