# Método classe x Método Estático

from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    
pessoa1 = Pessoa('maria', 19)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)

print(Pessoa.ehMaiorIdade(17))