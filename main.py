palavra = input('Digite uma palavra secreta: ').lower().strip()

for enter in range(50):
    print()

digitadas = []
acertos = []
erros  = 0

while True:
    advinha = ""
    for letra in palavra:
        if letra in acertos:
            advinha += letra
        else:
            advinha += '\u2588'
    
    print(f'Advinhe: {len(palavra)}letras: ')
    for letra in advinha:
        print(f'{letra} ', end=''""'')
    
    # Condicao de Vitoria
    print()
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

    #Desenhando a Forca
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O ')
    else:
        print('X')

    linha2 = ""
    if erros == 2:
        linha2 = " | "
    
    elif erros == 3:
        linha2 = " /| "
    
    elif erros >= 4:
        linha2 = " /|\ "
    
    print(f'X{linha2}')

    linha3 = ""
    if erros == 5:
        linha3 += " / "
    
    elif erros >= 6:
        linha3 += " / \ "
    
    print(f'X{linha3}')
    print(f'X\n=========')

    #Condicao de fim de jogos
    if erros == 6:
        print('Enforcado!')
        print(f'A palvra correta era {palavra}.')
        break

