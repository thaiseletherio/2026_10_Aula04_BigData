venda = float(input(f'Quanto você vendeu esse mês?'))
salario = float(input(f'Qual o seu salário?'))

if venda >= 1000:
    salario_bonus = salario + 150
    print (f'Parabéns! \nVocê ganhou um bônus de R$ 150,00 e vai receber R$ {salario_bonus:.2f} esse mês. ')

elif venda >= 500:
    salario_bonus2 = salario + 75
    print (f'Continue se esforçando. \nVocê recebeu um bônus de R$ 75,00 e vai receber R$ {salario_bonus2:.2f} esse mês.')

else:
    print (f'Fuem fuem fuem. Esse mês você ficou sem bônus. \nVai receber apenas {salario:.2f}.')