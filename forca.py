import random

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def exibir_forca(tentativas):
    palavra_escolhida = escolher_palavra(['desenvolvimento', 'tecnologia', 'lógica', 'programação', 'tendências'])
    for i in range(tentativas):
        print(f"Estágio {i+1} da forca:")
    print(f"A palavra correta era: {palavra_escolhida}")
    print("O boneco foi enforcado!")

def jogar():
    lista_palavras = ['desenvolvimento', 'tecnologia', 'lógica', 'programação', 'tendências']
    palavra_oculta = ['_' for _ in lista_palavras[0]]
    tentativas = 6
    letras_tentadas = set()
    
    print("Bem-vindo ao jogo da forca!")
    print("Você tem", tentativas, "tentativas para adivinhar a palavra.")
    
    while tentativas > 0 and '_' in palavra_oculta:
        letra_tentada = input("Digite uma letra: ").lower()
        if letra_tentada in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        letras_tentadas.add(letra_tentada)
        
        if letra_tentada in lista_palavras[0]:
            for i, letra in enumerate(lista_palavras[0]):
                if letra == letra_tentada:
                    palavra_oculta[i] = letra_tentada
            print("".join(palavra_oculta))
            if '_' not in palavra_oculta:
                print("Parabéns! Você adivinhou a palavra!")
                break
        else:
            tentativas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")
    
    if tentativas == 0:
        exibir_forca(tentativas)
    
    
    print("Obrigado por jogar! Espero que você tenha se divertido.")
    


jogar()
