import jwt
import datetime

# Chave secreta para assinar o token
secret_key = 'teste_1'

# Dados do usuário
user_data = {
    'email': 'usuario@example.com',
    'password': 'senha_segura'  # Note que, em um sistema real, você não deve armazenar senhas em texto simples
}

# Função para verificar as credenciais do usuário
def verify_credentials(email, password):
    # Lógica de verificação de credenciais
    # Aqui, vamos apenas verificar se o email e a senha correspondem aos dados fornecidos
    return email == user_data['email'] and password == user_data['password']

# Função para gerar o token JWT
def generate_token(email, password):
    if verify_credentials(email, password):
        payload = {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira em 1 hora
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return token
    else:
        return None

# Exemplo de uso
email = 'usuario@example.com'
password = 'senha_segura'
token = generate_token(email, password)

if token:
    print(f"Token gerado: {token}")
else:
    print("Credenciais inválidas")