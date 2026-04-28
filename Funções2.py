def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

#Criamos um dicionário vazio para armazenar as entradas de dados

info_usuario = {}

print("Digite as informações (ou 'Sair na chave para encerrar'): ")

while True:
    chave = input("Nome do campo ( ex: Profissão): ")
    if chave.lower() == 'sair':
        break
    valor = input(f"Salário {chave}: ")
    info_usuario[chave] = valor

#Usamos **B para desempacotar o dicionário com argumentos

exibir_info(**info_usuario)
