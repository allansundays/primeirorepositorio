# Conversão metros em centímetros e em milímetros
n1 = float(input('Olá, Quantos metros ? '))
cm = n1 * 100
mm = n1 * 1000
print(f'{n1} metros equivale a {cm:.0f} cm e a {mm:.0f} mm')

dm = n1 * 10
dam = n1 / 10
hm = n1 / 100
km = n1 / 1000
print(f'{n1} m equivale a:\n{dm:.0f} dm \n{dam:.0f} dam \n{hm:.0f} hm \n{km:.0f} km ')