def question():
    return input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuárion\n" +
            "<P> - Para Pesquisar um usuárion\n" +
            "<I> - Para Excluir um usuárion\n" +
            "<I> - Para Listar um usuárion: ").upper()

def insert(user):
    user[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(), 
                                                  input("Digite a última data de acesso: "),
                                                  input("Digite a última estação acessada: ").upper()]