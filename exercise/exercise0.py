preco_unitario = 10
desconto1 = 0.1
desconto2 = 0.2
quantidade = eval(input("Digite a quantidade que vai comprar: "))

if(quantidade <= 10):
    valor_final = preco_unitario*quantidade
elif(quantidade <= 20):
    valor_final = preco_unitario*quantidade*(1-desconto1)
else:
    valor_final = preco_unitario*quantidade*(1-desconto2)
    
print(f'o valor final da compra é: {valor_final}')