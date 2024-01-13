from time import sleep
print('='*15, end='')
print(' Lojas Fique Liso ', end='')
print('='*15)
preço = float(input('Valor total das compras R$ '))
desc10 = ((10 / 100) * preço)
desc5 = ((5 / 100) * preço)
juros = ((20 / 100) * preço)
print('FORMAS DE PAGAMENTO \n' 
'[ 1 ] à vista dinheiro/cheque \n' 
'[ 2 ] à vista cartão \n'
'[ 3 ] 2x no cartão\n'
'[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual opção de pagamento?'))
print('Aguarde.....')
sleep(2)
if opcao == 1:
    print('Sua compra de R$ {:.2f}, vai sair por R${:.2f}'.format(preço,preço-desc10))
elif opcao == 2:
    print('Sua compra de R$ {:.2f}, vai sair por R${:.2f}'.format(preço,preço-desc5))
elif opcao == 3:
    print('Sua compra é de R$ {:.2f}'.format(preço))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {:.0f}x de R${:.2f} COM JUROS\n'
    'valor total com Juros R${:.2f}'.format(parcelas,((juros+preço)/parcelas),juros+preço))
else:
    print('Opção Inválida')
