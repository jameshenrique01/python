a = 10
b = 5
soma = a + b
sub  = a - b
mult = a * b
div  = a / b
resto = a % b

#Print com texto + tipo
#O Print não consegue printar um valor com um texto junto, por isso se utiliza str para printar os dois
print('Com STR\n')
print('Soma: ' + str(soma) + '\nSubtração: ' + str(sub) + '\nMultiplicação: ' + str(mult) + '\nDivisão: ' + str(div)
      + '\nResto: ' + str(resto))

#também pode ser utilizado o .format(variavel)
#no texto deve ser incluso as {} para que o .format atribua o valor da variavel
#exemplo:
print('\nCom .format()')
print('\nSoma: {}'.format(soma) + '\nSubtração: {}'.format(sub) + '\nMultiplicação: {}' .format(mult) +
      '\nDivisão: {}' .format(div) + '\nResto: {}' .format(resto))

#agora de forma mais simplificada
print('\nCom .format()')
print('\nSoma: {soma}  \nSubtração: {sub}  \nMultiplicação: {mult}  \nDivisão: {div}  \nResto: {resto}'
      . format(soma=soma, sub=sub, mult=mult, div=div, resto=resto))

print(int(div)) #converte o tipo de uma variavel para outra

#exemplo:
x = '1' #o x está atribuindo um valor no tipo texto(string)
print(type(x)) #mostra o tipo da variavel
soma2 = int(x) + 1 #transforma o x de str para int e adiciona + 1
print(soma2)



