from Introducao.modelos.restaurante import Restaurante

restaurante_praça = Restaurante('praça','Gourmet')
restaurante_mexicano = Restaurante('mexican food','Mexicana')
restaurant_japones = Restaurante('JapaFood','japones')
restaurante_mexicano.alterar_estado()

restaurante_praça.receber_avaliacao('lorenzo',10)
restaurante_praça.receber_avaliacao('joao',9)
restaurante_praça.receber_avaliacao('maria',8)

def main():
    Restaurante.listar_restaurantes()

if __name__== "__main__":
    main()