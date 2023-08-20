class Usuario():
    """Referencia usuários"""
    # método de inicialização
    def __init__(self, primeiro_nome, ultimo_nome, telefone, email):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.telefone = telefone
        self.email = email

    # método (descrição)
    def descricao_usuario(self):
        print('\nDados de ' + self.primeiro_nome.title() + ' ' + self.ultimo_nome.title() + ':')
        print('Telefone: ' + self.telefone)
        print('E-mail: ' + self.email)

    # método (saudação)
    def saudacao_usuario(self):
        print('\nEi, ' + self.primeiro_nome.title() + ' ' + self.ultimo_nome.title() + '! Como vai você?')


# Instâncias
usuario1 = Usuario('Perroni', 'Pardinho', '99999-9999', 'perroniparndino@gmail.com')
usuario2 = Usuario('Josekelly monique', 'celino', '99999-9999', 'kelly.celino05@gmail.com')
usuario3 = Usuario('fulano', 'de tal', '99999-9999', 'fulanodetal@gmail.com')

usuario1.descricao_usuario()
usuario2.descricao_usuario()
usuario3.descricao_usuario()

usuario1.saudacao_usuario()
usuario2.saudacao_usuario()
usuario3.saudacao_usuario()