from modelos.livro import Livro

sr_aneis = Livro('O Senhor Dos Aneis - Sociedade Do Anel','J.R.R.TOLKIEN',1954)
nome_do_vento = Livro('O Nome do Vento', 'Patrik Rotfus',2007)


def main():
    Livro.listar_livros()
    sr_aneis.emprestar()
    Livro.listar_livros()
    sr_aneis.emprestar()

if __name__ == '__main__':
    main()