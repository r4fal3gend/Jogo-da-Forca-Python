from atexit import register
from pydoc import stripid
from funcoes import limparTela, menuApresentacao, ganhou, perdeu, printarHistorico
import time
from datetime import datetime

limparTela()
menuApresentacao()
time.sleep(2)
limparTela()

nomeDesafiante = input("Quem vai desafiar? ")
nomeDesafiado = input("Quem vai ser desafiado? ")

limparTela

print("As seguintes informações devem ser completadas pelo Desafiante: ")
palavraChave = input("\nDigite a Palavra Chave:").upper().strip()

primeiraDica = input("\nDigite a Dica 1: ")
segundaDica = input("\nDigite a Dica 2: ")
terceiraDica = input("\nDigite a Dica 3: ")

letrasDigitadas = []
letrasCertas = []
erros = 0
limparTela()

print("Bem Vindo", nomeDesafiado)
print("----------------------------------")

while True:
    key = ''
    for letra in palavraChave:
        key += letra if letra in letrasCertas else "_ "
    print("Acerte a Palavra:", key)
    if key == palavraChave:
        ganhou()
        break
    print('''\nDigite "0" para receber dicas''')
    tentativa = input ("\nDigite uma letra:").upper().strip()
    limparTela()
    if tentativa == '0':
        escolherDica = input ('''
(1) Para a Dica 1.
(2) Para a Dica 2.
(3) Para a Dica 3.

Selecione uma opção: 
''')
        if escolherDica == '1':
            print("\nDica 1: ", primeiraDica)
            time.sleep(2)
            limparTela()
        elif escolherDica == '2':
            print("\nDica 2: ", segundaDica)
            time.sleep(2)
        elif escolherDica == '3':
            print("\nDica 3: ", terceiraDica)
            time.sleep(2)
            limparTela()
        else:
            print("Opção Inválida!\n")
            time.sleep(2)
            limparTela()

    try:
        letrasDigitadas
    except:
        print("Caracter Inválido!\n")

    if tentativa in letrasDigitadas:
        print("Você já tentou essa letra!\n")
        erros -= 1
    else:
        letrasDigitadas += tentativa

    if tentativa in palavraChave or tentativa == '0':
        letrasCertas += tentativa
    else:
        erros += 1
        print("Essa letra não está na palavra!\n")

    if erros >= 6:
        print('''
I==:==
I  :
I  O        ENFORCADO!
I /|\\
I / \\
------
''')
        time.sleep(2)
        break

    print("I==:==\nI :  ")
    print("I O  " if erros >= 1 else "I")

    linhaDois = ""
    if erros == 2:
        linhaDois = " |  "
    elif erros == 3:
        linhaDois = "/|  "
    elif erros >= 4:
        linhaDois = "/|\\  "
    print("I%s" % linhaDois)

    linhaTres = ""
    if erros == 5:
        linhaTres = "/  "
    elif erros >= 6:
        linhaTres =  "/ \  "
    print("I%s" % linhaTres)
    print("I\n---------")

limparTela()
if key == palavraChave:
    ganhou()
    time.sleep(2)
    limparTela()

print("A Palavra Chave era :", palavraChave)
registro = open ("registro.txt", "w")

if key == palavraChave:
    registro.write("O(a) vencedor(a) foi %s" % nomeDesafiado)
else:
    registro.write("O(a) vencedor(a) foi %s" % nomeDesafiante)

registro = open("registro.txt", "r")
conteudo = registro.read()
print(conteudo)

input("\nPrecione Enter para continuar")
limparTela()

historicoPartidas = []
dataAtual = datetime.today().strftime("%d/%m/%Y - %H:%M")

arquivo = open("historico.txt", "a")
historicoPartidas.append(dataAtual+ " -> " +nomeDesafiante+ " VS " +nomeDesafiado+ " -> "+conteudo+ " -> " + "Palavra:" +palavraChave+ "\n")
arquivo.write(''.join(historicoPartidas))
arquivo.close()

print('''
(1) Para ver o Histórico.
(2) Para deletar o Histórico.
(0) Para Sair: 
''')

verHistorico = input("\nDigite uma opção:")

if verHistorico == '1':
    printarHistorico()
    quit()
elif verHistorico == '2':
    del historicoPartidas
    arquivo = open("historico.txt", "w")
    arquivo.close()
    limparTela()
    print("Histórico deletado com sucesso!")
    time.sleep(2)
    quit()
elif verHistorico == '0':
    limparTela
    quit()
