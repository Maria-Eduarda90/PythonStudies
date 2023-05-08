class Pessoa:
    def __init__(self, nome, endereco):
        self.set_nome(nome)
        self.set_endereco(endereco)

    def set_nome(self, nome):
        self.nome = nome
    
    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_nome(self):
        return self.nome
    
    def get_endereco(self):
        return self.endereco

pessoa1 = Pessoa("Maria", "Rua 03208")
pessoa2 = Pessoa("Elisa", "Rua 03208")

print(f'Nome: {pessoa1.get_nome()}, Endereco: {pessoa1.get_endereco()}')
print(f'Nome: {pessoa2.get_nome()}, Endereco: {pessoa2.get_endereco()}')