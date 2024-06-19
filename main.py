# Aluno: Pedro Segatto
# RA: 1136047

import os, time


def limparTela(tempo):
    time.sleep(tempo)
    os.system("cls")


def mostrarPalavraChave(palavra, letrasTentadas):
    palavraEscondida = " "
    for letra in palavra:
        if letra in letrasTentadas:
            palavraEscondida += letra
        else:
            palavraEscondida += "*"
    return palavraEscondida

def desenharForca(erros):
    if erros == 1:
        print("""
       -----+
       |    0
       |
       |
       |
    ___|___""")
    elif erros == 2:
        print("""
       -----+
       |    0
       |    |
       |
       |
    ___|___""")  
    elif erros == 3:
        print("""
       -----+
       |    0
       |    |
       |   /
       | 
    ___|___""")
    elif erros == 4:
        print("""
       -----+
       |    0
       |    |
       |   / |
       |
    ___|___""")
    elif erros == 5:
        print("""
       -----+
       |    0
       |   /|
       |   / |
       |
    ___|___""")
    else:
        print("""
       -----+
       |    0
       |   /|)
       |   / |
       |
    ___|___""")
        


def jogoForca():
    limparTela(1)
    print("    Bem vindos ao Jogo da Forca!!!   ")
    desafiante = input("Nome do Desafiante:")
    competidor = input("Nome do Competidor:")
    limparTela(1)


    palavraChave = input(f"{desafiante}, insira a palavra chave: ").lower()
    dica1 = input("Dica 1:")
    dica2 = input("Dica 2:")
    dica3 = input("Dica 3:")
    dicasRestantes = 3
    limparTela(1)


    qntLetras = len(palavraChave)
    print(f"Olá {competidor}! ")
    print(f"A palavra chave tem {qntLetras} letras!")
    limparTela(2)
 
    erros = 0
    letrasTentadas = []

    while True:
        palavraSecreta =  mostrarPalavraChave(palavraChave, letrasTentadas)
        print(f'Palavra: {palavraSecreta}\nErros: {erros}/6')

        if '*' not in palavraSecreta:
            print(f'Parabéns, {competidor}!! Você adivinhou.')
            break
        elif erros == 6:
            print('Você perdeu, suas tentativas acabaram.')
            limparTela(5)
            break
        
        print('Escolha uma opção:\n(1) Jogar\n(0) Pedir Dica')
        escolha = input('Insira sua escolha: ')
        limparTela(0)
        if escolha == '1':  
            print(f'Letras já jogadas: {letrasTentadas}')
            letra = input("Digite uma letra: ").lower()
            if len(letra) == 1:
                if letra in letrasTentadas:
                    print('Você já usou essa letra, tente outra.')
                    limparTela(1)
                else:
                    letrasTentadas.append(letra)
                    if letra in palavraChave:
                        limparTela(0)
                        print(f"Letra '{letra}' encontrada: {mostrarPalavraChave(palavraChave, letrasTentadas)}")
                        limparTela(2)
                    elif letra not in palavraChave:
                        erros += 1
                        limparTela(0)
                        print(f"Letra '{letra}' não encontrada. Erros: {erros}")
                        desenharForca(erros)
            else:
                print('Apenas uma letra por vez!')
                limparTela(2)
                
        if escolha == "0":
            if dicasRestantes == 3:
                print(f'Dica 1:{dica1}')
                dicasRestantes -= 1
                limparTela(3)
            elif dicasRestantes == 2:
                print(f'Dica 2:{dica2}')
                dicasRestantes -= 1
                limparTela(3)
            elif dicasRestantes == 1:
                print(f'Dica 3:{dica3}')
                dicasRestantes -= 1
                limparTela(3)
            else:
                print('Suas dicas acabaram!')
                limparTela(3)


    jogarNovamente = input("(1)Jogar Novamente\n(0)Sair\nDeseja continuar jogando? ")
    if jogarNovamente == '1':
        jogoForca()
    else:
        quit()
jogoForca()