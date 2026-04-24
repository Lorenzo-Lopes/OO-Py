from modelos.cardapio.item_cardapio import Item_cardapio

class Bebida(Item_cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome,preco)
        self._tamanho = tamanho

    def aplica_desconto(self):
        self._preco -= self._preco*0.05