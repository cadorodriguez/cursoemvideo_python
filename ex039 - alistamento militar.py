from datetime import date
anoNasc = int(input('Qual ano do seu Nascimento?'))
sexo = str(input('Qual seu sexo? M ou F')).upper()
atual = date.today().year
if sexo == 'M':
    if (atual - anoNasc) < 18:
        print('Quem nasceu em {} tem em {}, {} anos e deve de alistar em {}'.format(anoNasc,atual,(atual-anoNasc),anoNasc+18))
    elif (atual-anoNasc) > 18:
        print('Quem nasceu em {} tem em {}, {} anos e deveria ter se alistado em {}'.format(anoNasc,atual,(atual-anoNasc),(anoNasc+18)))
    elif (atual-anoNasc) == 18:
        print('Quem nasceu em {}, tem {} e deve procurar o serviço de alistamento esse ano'.format(anoNasc, atual-anoNasc))
else:
    print('No Brasil o alistamento só é obrigatório para jovens do sexo Masculino')