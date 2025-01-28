def ler_arquivo_palavras():
    arquivo = open('D:\Oracle\Python\Python Completo do Zero ao Avancado\Forca\palavras.txt','r')
    lista_palavras = []
    try:
        
        for palavra in arquivo:
            # print(palavra)
            palavra = palavra.replace('\n', '').strip()
            lista_palavras.append(palavra)
        
        return lista_palavras
    
    except:
        print(f"Erro Ao Tentar ler o arquivo. ")


