import whois
dominio = input('Alvo: ')
consulta_whois = whois.whois(dominio)

print(consulta_whois.text)