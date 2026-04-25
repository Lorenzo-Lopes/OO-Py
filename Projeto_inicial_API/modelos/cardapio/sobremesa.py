from modelos.cardapio.item_cardapio import Item_cardapio

class Sobremesa(Item_cardapio):
    def __init__(self, nome, preco,tipo,tamanho,descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao


    def __str__(self):
        return self._nome

    def aplica_desconto(self):
        self._preco -= self._preco*0.15

