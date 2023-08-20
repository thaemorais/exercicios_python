class Restaurante():
    """Representa os restaurantes"""

    # metodo construtor da classe, serve para inicializar os atributos da classe
    def __init__(self, nome, tipo):
        """Inicializa os atributos restaurante_nome e tipo_cozinha"""
        self.nome = nome  # atributo
        self.tipo = tipo # atributo

    # método
    def restaurante_descricao(self):
        """Mostra as informações do restaurante"""
        print('O restaurante se chama '+ self.nome.title() + ' e é especializado em ' + self.tipo.title())

    # método
    def restaurante_aberto(self):
        """Mostra que o restaurante está aberto"""
        print('O restaurante ' + self.nome.title() + ' está aberto!')


# instâncias
restaurante1 = Restaurante("Coliseu", "comida italiana")
restaurante2 = Restaurante('Mineirao', 'churrascaria')
restaurante3 = Restaurante('wburguer', 'comida mexicana')


# chamadas
restaurante1.restaurante_descricao()
restaurante2.restaurante_descricao()
restaurante3.restaurante_descricao()

