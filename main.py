from jogo import *
import BancoDados as bd

def mostra_menu():
    print('-'*50)
    print('| 1 - Jogar Jogo da Forca \t\t\t  |')
    print('| 2 - Mostrar Pontuação do Jogo\t\t\t  |')
    print('| 3 - Sair' + ' ' *40 + '|')
    print('-'*50)

def main():
    while True:
        try:

            conexao = bd.conectar()
            bd.criar_tabela(conexao)

            mostra_menu()
            escolha = int(input('Escolha uma das opções acima para prosseguir: '))
            
            while escolha not in(1, 2, 3):
                print('Por favor escolha uma opção válida.')
                mostra_menu()
                escolha = int(input('Escolha uma das opções acima para prosseguir: '))
            
            if escolha == 1:
                jogar()
                jogar_novamente()
                
            elif escolha == 2: 
                print('SCORE')
                dados = bd.listar_dados()

                if not dados:
                    print('Score Vazio')
                
                else:
                    i = 1
                    for linha in dados:
                        print(f'{i} º Nome: {linha[1]} - Score: {linha[2]}')
                        i += 1
                
            elif escolha == 3:
                print('Saindo do Menu ....')
                break

        except ValueError:
            print('-'*50)
            print('Por favor digite somente números.')
    
    bd.desconectar(conexao)

main()

