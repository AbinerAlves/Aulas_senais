#Parâmetros com valor padrão (default)
def saudacao(nome, mensagem = "Bem vindo!"):
    print(f"Olá, {nome}! {mensagem}")
nome = str(input("Digite seu nome: "))
saudacao(nome)
#Argumentos nomeados(keyword args)
def criar_usuario(nome, idade, admin = False):
    print(f"{nome} | {idade} anos | admin={admin}")
idade = str(input("Digite sua idade: "))   
criar_usuario(nome, idade)