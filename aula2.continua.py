#Continuação da aula 2
#Para interação com o usuário, deve-se utilizar input para que ele atribua um valor
#lembre-se que precisa converter para int as variaveis, conforme o exemplo abaixo
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
sub  = a - b
mult = a * b
div  = a / b
resto = a % b

print('\nSoma: {soma}  \nSubtração: {sub}  \nMultiplicação: {mult}  \nDivisão: {div}  \nResto: {resto}'
      . format(soma=soma, sub=sub, mult=mult, div=div, resto=resto))