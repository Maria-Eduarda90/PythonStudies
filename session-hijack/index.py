import requests
session = requests.Session()
response = session.get('https://github.com/')
print(session.cookies.get_dict())