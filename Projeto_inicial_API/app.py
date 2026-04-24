from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
# cafe = Bebida('Cafezinho','2,00','100 ml')
pao_com_manteiga = Prato('Pao na Chapa',5,'Melhor pao da cidade.')
restaurante_praca.add_item_cardapio(Bebida('Cafezinho',2,'100 ml'))
restaurante_praca.add_item_cardapio(pao_com_manteiga)
pao_com_manteiga.aplica_desconto()

def main():
 

    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()