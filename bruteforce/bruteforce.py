import dns.resolver

resolved = dns.resolver.Resolver()

arquivo = open("C:/Users/Doctor/Documents/programas/program_in_python/bruteforce/wordlist.txt", "r")
subdominios = arquivo.read().splitlines()

alvo = "bancocn.com"

for subdominio in subdominios:
    try:
        sub_alvo = subdominio + "." + alvo
        resultado = resolved.resolve(sub_alvo, "A")
        for ip in resultado:
            print(sub_alvo, "->", ip)
    except:
        pass