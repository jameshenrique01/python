#descobrindo se um número é par ou impar com condicional

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

# or apenas para saber se foi digitado algum número digitado ( se alguma afirmação for verdadeira)
# or not apenas para saber se os valores são par ou não
if resto_a == 0 or not resto_b:
    print('Foi digitado um número par')
else:
    print('Nenhum número par foi digitado')