class Conta:
    def __init__(self, numero, cpf, nomeTitulo, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitulo = nomeTitulo
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'numero: {self.numero}\ncpf: {self.cpf}\nsaldo: {self.saldo}')

def main():
    c1 = Conta(1, 1, "João", 0)
    c1.depositar(300)
    saque = c1.sacar(100)
    c1.gerar_extrato()
    print(f'O saque foi realizado? {saque}')

if __name__ == "__main__":
    main()
