from datetime import datetime

class Order:

    def __init__(self,preco,quantidade):
        self.preco = preco
        self.quantidade = quantidade
        self.momento = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    def total(self):
        print(self.momento)
        return self.preco * self.quantidade
