from abc import ABC,abstractmethod


class Item_cardapio(ABC):
    def __init__(self, nome,preco):
        self._nome= nome
        self._preco = preco
        
    def __str__(self):
        return self._nome
    
    @abstractmethod
    def aplica_desconto(self):
        pass