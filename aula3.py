#aprendendo a utilizar condicionais

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#condicional
if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c: #elif é um else if
    print('O maior número é {}' .format(b))
else:
    print('O maior número é {}' .format(c))





