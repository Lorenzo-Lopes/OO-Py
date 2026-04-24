from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
cafe = Bebida('Cafezinho','2,00','100 ml')
pao_com_manteiga = Prato('Pao na Chapa','5,00','Melhor pao da cidade.')
def main():
    print(cafe)
    print(pao_com_manteiga)

if __name__ == '__main__':
    main()