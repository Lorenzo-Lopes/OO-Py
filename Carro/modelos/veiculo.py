class Veiculo:
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        estado ='Ligado' if self._ligado else "Desligado"
        return f'Modelo: {self._modelo} da Marca: {self._marca} esta {estado}'