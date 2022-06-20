from gestao_arquivo import Arquivo
from elo_prob import EloProb
from auxiliar import lista_times, checkTeam
from time import sleep
from elo_atualizacao import EloAtualizacao

def menu(): # função para mostrar o menu            
    print('\n')
    print('1 - Criar arquivo')
    print('2 - Listar times')
    print('3 - Adicionar time')
    print('4 - Calcular probabilidade de vitória')
    print('5 - Atualizar Elo Rating')
    print('6 - Sair')
    
    opcao = int(input('Escolha uma opção: '))
    return opcao

opcao = menu() # chamada da função menu
while True: 
    if opcao == 1: #criar arquivo
        Arquivo('EloRating.csv').criar_arquivo()
        opcao = menu()
    elif opcao == 2: #listar times
        print('\n')
        print(lista_times())
        opcao = menu()
    elif opcao == 3: #adicionar time
        time = input('Digite o nome do time: ')
        checkTeam(time)
        opcao = menu()
    elif opcao == 4: #calcular probabilidade de vitoria
        lista_times()
        print('\n')
        time1 = input('Digite o time 1: ')
        time2 = input('Digite o time 2: ')
        #verificando se os times estão no arquivo
        checkTeam(time1)
        checkTeam(time2)
        winner = EloProb(time1, time2).prob()
        prob = EloProb(time1, time2)
        print(prob)
        sleep(2)
        print('\n')
        print('Você deseja calcular a probabilidade de vitória de outro time? (S/N)')
        opcao = input('Opção: ')
        if opcao.upper() == 'S':
            #chamar a opção 4 novamente
            opcao = 4
        else:
            opcao = menu()
    elif opcao == 5: #recalcular elo rating
        #Listar os times
        lista_times()
        print('\n')
        #Receber os times e o vencedor
        time1 = input('Digite o time 1: ')
        time2 = input('Digite o time 2: ')
        winner = input('Digite o vencedor: ')
        checkTeam(time1)
        checkTeam(time2)
        #Atualizar o Elo Rating
        EloAtualizacao(time1, time2, winner).atualizar()
        print('\n')
        print('Você deseja recalcular o Elo Rating de outro time? (S/N)')
        opcao = input('Opção: ')
        if opcao.upper() == 'S':
            #chamar a opção 3 novamente
            opcao = 5
        else:
            opcao = menu()