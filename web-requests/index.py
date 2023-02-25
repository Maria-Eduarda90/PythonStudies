import requests

try:
    req = str(input('digite uma url para a requisição: '))
    request = requests.get(req)
    print(request.text)
except Exception as err:
    print('Requisição deu erro: ', err)
