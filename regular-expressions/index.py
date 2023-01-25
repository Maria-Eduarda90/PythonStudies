import re
import requests

req = requests.get('https://zecoxinha.com.br/')

pattern = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)

if pattern:
    print(pattern)
else:
    print("padrão não encontrado")