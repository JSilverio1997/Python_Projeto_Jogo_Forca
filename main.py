import desenhos as d 

palavra = input('Digite uma palavra secreta: ').lower().strip()

for enter in range(50):
    print()

digitadas = []
acertos = []
erros  = 0

while True:
    advinha = d.imprimir_palavra_secreta(palavra, acertos)
    if advinha == palavra:
        print('Você acertou!')
        break

    #Tentativas
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já usou essa letra!')
        continue
    
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        
        else:
            erros += 1
            print('Você errou!')

    d.desenhar_forca(erros)

    #Condicao de fim de jogos
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra correta era {palavra}.')
        break

