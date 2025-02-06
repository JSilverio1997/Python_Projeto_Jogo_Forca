def imprimir_palavra_secreta(palavra, acertos):
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
    return advinha

def desenhar_forca(erros):
    score = 1000
    #Desenhando a Forca
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O ')
        score = 800

    else:
        print('X')

    linha2 = ""
    if erros == 2:
        linha2 = " | "
        score = 600
    
    elif erros == 3:
        linha2 = " /| "
        score = 400
    
    elif erros >= 4:
        linha2 = " /|\ "
        score = 200
    
    print(f'X{linha2}')

    linha3 = ""
    if erros == 5:
        linha3 += " / "
        score = 100
    
    elif erros >= 6:
        linha3 += " / \ "
        score = 0
    
    return score

    print(f'X{linha3}')
    print(f'X\n=========')