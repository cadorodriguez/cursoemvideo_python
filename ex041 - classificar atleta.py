from    datetime import date
ano = int(input('Qual o ano de nascimento:'))
anoAtual = date.today().year
idade = anoAtual-ano
if idade <= 9:
    print('O atleta tem {} anos.\n Classificação: MIRIM'.format(idade))
elif 10 > idade <= 14:
    print('O atleta tem {} anos.\n Classificação: INFANTIL'.format(idade))
elif 15 > idade <= 19:
    print('O atleta tem {} anos.\n Classificação: JÚNIOR'.format(idade))
elif 20 > idade <= 25:
    print('O atleta tem {} anos.\n Classificação: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos.\n Classificação: MASTER'.format(idade))



