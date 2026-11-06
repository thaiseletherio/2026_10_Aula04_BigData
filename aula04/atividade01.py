#Entrada
valor_conta = int(input('Valor da compra:' ))

#Verificação e saída
if valor_conta > 250:
    desconto = valor_conta * 0.16
    valor_conta = valor_conta - desconto
    print (f'A sua conta foi: R$ {valor_conta:.2f} \nO seu desconto foi: R$ {desconto}')

else: 
    print(f'A sua compra foi R$ {valor_conta:.2f}.')
