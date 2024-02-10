import dns.resolver
dominio = input("Alvo: ")
registros = ["AAAA", "A", "MX", "NS"]

for registro in registros:
    result = dns.resolver.query(dominio, registro, raise_on_no_answer=False)

    if result.rrset is not None:
        print(result.rrset)