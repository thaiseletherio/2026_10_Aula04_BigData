
#entrada
pontos = int(input('Quantos pontos você fez no jogo? '))

if pontos >= 100:
    pontos = pontos + 10
    print (f'Excelente! Você tem {pontos} pontos agora!')
elif pontos >= 50:
    pontos = pontos + 5
    print (f'Muito bom. Você tem {pontos} pontos agora.')

else:
    print (f'Tente outra vez. Você tem {pontos} agora.')    