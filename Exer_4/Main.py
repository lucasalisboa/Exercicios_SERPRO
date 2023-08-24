quantidade = []
preco = []

with open("teste.txt") as f:
    for line in f:
        quant, pre = line.split(" ")
        quantidade.append(float(quant))
        preco.append(float(pre))

for v in range(len(quantidade)):
    print(quantidade[v]*preco[v])