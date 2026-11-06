ano_nascimento = int(input('Informe o ano de nascimento: '))

idade = 2026 - ano_nascimento

if idade >= 18:
    print ('Parabéns, você é maior de idade. Entre.')

else:
    print ('Você é menor de idade e não pode entrar aqui.')