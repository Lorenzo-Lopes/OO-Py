from modelos.livro import Livro

sr_aneis = Livro('O Senhor Dos Aneis - Sociedade Do Anel','J.R.R.TOLKIEN',1954)
nome_do_vento = Livro('O Nome do Vento', 'Patrik Rotfus',2007)


def main():
    Livro.listar_livros()
    sr_aneis.emprestar()
    Livro.listar_livros()
    sr_aneis.emprestar()

    ano_publicacao = int(input("Informe o ano do livro que deseja alugar: "))
    Livro.verificar_disponibilidade(ano_publicacao)

if __name__ == '__main__':
    main()