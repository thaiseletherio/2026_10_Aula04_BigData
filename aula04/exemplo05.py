#entrada
valor = float(input(f'Quanto foi a sua compra hoje? '))
fidelidade = input('Você tem nosso programa de fidelidade? [S / N] ').lower()[0]
print (fidelidade)


if valor > 100 or fidelidade == 's':
    print('Parabéns, você ganhou nosso brinde especial!')

else:
    print ('Obrigada por comprar conosco, mas você não ganhou brinde =P') 

#o .lower() força a resposta para o minúsculo e o colchete fala que vai pegar o primeiro caracter do texto que a pessoa digitar
