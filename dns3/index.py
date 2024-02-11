import dns.resolver

dns = dns.resolver.resolve
dominio = input("Alvo: ")
result = dns(dominio, 'A')

for ipval in result:
    print('IP: ', ipval.to_text())
    ip_alvo = ipval.to_text()

print('---------------')

try:
    result = dns(dominio, 'CNAME')
    for cnameval in result:
        print('CNAME: ', cnameval.target)

except:
    print('Não existe')

print('---------------')

result = dns(dominio, 'AAAA')

for val in result:
    print('AAAA: ', ipval.to_text())

print('---------------')

try:
    result = dns(ip_alvo+'.in-addr.arpa', 'PTR')

    for val in result:
        print('PTR: ', val.to_text())
except:
    print('Não existe')

print('---------------')

result = dns(dominio, 'NS')

for val in result:
    print('NS: ', val.to_text())

print('---------------')

result = dns(dominio, 'MX')

for exdata in result:
    print('MX: ', exdata.to_text())

print('---------------')

result = dns(dominio, 'SOA')

for val in result:
    print('SOA: ', val.to_text())

print('---------------')

result = dns(dominio, 'TXT')

for val in result:
    print('TXT: ', val.to_text())