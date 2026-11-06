
#entrada
pontos = int(input('Quantos pontos você fez no jogo? '))

if pontos >= 100:
    pontos = pontos + 10
    print (f'Excelente! Você tem {pontos} pontos agora!')
if pontos >= 50:
    pontos = pontos + 5
    print (f'Muito bom. Você tem {pontos} pontos agora.')

else:
    print (f'Tente outra vez. Você tem {pontos} agora.')    

# Se for mais de uma condição, sempre use o elif. elif é um if condicional (se não for esse if, então se...). 
# Se usar o if, nesse caso em que são condições diferentes,  ele roda uma soma de ifs e não as condições.