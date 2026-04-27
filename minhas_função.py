geral = "Essa variavel posso chamar onde quiser"
def minha_funçao():
    print("Essa é minha função")
    local = "Essa váriavel só pode ser ultilizada na função"

#chamando minha fução
minha_funçao()
print(geral)   

#print geral

nome = "Alan" #global

def saudacao():
    sobrenome = "code" # Local
    print(f"Olá, {nome} {sobrenome}")

    saudacao()

    def somar(n1, n2): #n1 e n2 são parâmetros
        print(f"A soma é {n1 + n2}")

    somar(6, 40)# 6 e 40 são os argumentos 


def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

#Uso:
preco_hospedagem = 49.9
print(formatar_real(preco_hospedagem)) #R$ 49,90

    
