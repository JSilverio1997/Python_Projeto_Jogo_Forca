import desenhos as d 
from Arquivos import ler_arquivo_palavras
from random import choice
import BancoDados as bd

def jogar_novamente():
  escolha = input('Você deseja jogar novamente (S/N ) ? ') .strip().upper()  
  while escolha not in('S', 'N'):
      print('-'*50)
      print('Por favor escolha uma opção válida. ')
      escolha = input('Você deseja jogar novamente (S/N ) ? ').strip().upper() 
  
  while escolha == 'S':
      jogar()
      escolha = input('Você deseja jogar novamente (S/N ) ? ') .strip().upper()
  
  if escolha == 'N':
      print('Retornando ao Menu Principal.')

def jogar():

    nome = input('Digite o seu nome: ')
    while nome.isalpha() is False:
        print('-'*50)
        print('Por favor digite o nome corretamente.')
        nome = input('Digite o seu nome: ')
        
    lista_palavras = list()
    lista_palavras = ler_arquivo_palavras()

    palavra_sorteada = choice(lista_palavras)

    for enter in range(50):
        print()

    digitadas = []
    acertos = []
    erros  = 0

    while True:
        advinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
        if advinha == palavra_sorteada:
            print('Você acertou!')
            break

        #Tentativas
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou essa letra!')
            continue
        
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            
            else:
                erros += 1
                print('Você errou!')

        score = d.desenhar_forca(erros)

        #Condicao de fim de jogos
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada}.')
            break
    
    bd.inserir_dado(nome, score)

