import bcrypt

hashed_password = b'$1a$10$fhnNN9OwQMep7AuUQ6tEReStfqckunkgWE1ernq230668tFXA9q.K'

def load_wordlist(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return [line.strip() for line in file]

def check_password_from_wordlist(hashed_password, wordlist):
    for password in wordlist:
        print(f"Verificando senha: {password}")
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print(f"A senha correta é: {password}")
            return
    print("Nenhuma senha da wordlist corresponde ao hash.")

wordlist = load_wordlist('rockyou.txt')
check_password_from_wordlist(hashed_password, wordlist)