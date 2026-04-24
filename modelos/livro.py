class Livro:
    livros =[]
    def __init__(self,titulo,autor,ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel=True
        Livro.livros.append(self)

    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'Livro: {livro._titulo}, escrito por: {livro._autor}, lancado em: {livro._ano_publicacao} ')


    
    def altera_disponibilidade(self):
        self._disponivel = not self._disponivel

    def emprestar(self):
        if self._disponivel:
            self.altera_disponibilidade()
            return print(f'Voce pode emprestar {self._titulo}' )
        return print(f'O titulo: {self._titulo} Não estar dispponivel no momento.')

    
