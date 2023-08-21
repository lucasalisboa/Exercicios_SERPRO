import Order

preco = float(input("Digite o preco"))
quantidade = int(input("Digite a quantidade"))

novo_pedido = Order.Order(preco,quantidade)
conta = novo_pedido.total()
print(conta)