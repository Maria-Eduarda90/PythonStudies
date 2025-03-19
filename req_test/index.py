import requests
import json

url = "https://login-back.alwaysfitapp.com.br/api/login"

# Dados de entrada malformados
payloads = [
    {"email": "", "password": ""},          # Campos vazios
    {"email": "test@example.com", "password": ""},  # Senha vazia
    {"email": "", "password": "password123"},      # Email vazio
    {"email": "test@example.com", "password": "password123"},  # Dados válidos
    {"email": "test@example.com<script>alert('xss')</script>", "password": "password123"},  # Tentativa de XSS
    {"email": "test@example.com", "password": "password123' OR '1'='1"},  # Tentativa de SQL Injection
]

for payload in payloads:
    response = requests.post(url, json=payload)
    print(f"Payload: {payload}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)