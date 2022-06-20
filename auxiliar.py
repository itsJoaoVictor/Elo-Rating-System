import re
from gestao_arquivo import Arquivo

#importando sistema de Elo Rating 
elo_rating = Arquivo('EloRating.csv').lendo_arquivo()

#Definindo um Elo Rating inicial
elo_rating_inicial = 1500
 
def checkTeam(time): #função para verificar se o time está no arquivo
    if time in elo_rating['Time'].values:
        return True
    else:
        #adicionando o time no arquivo caso não exista
        elo_rating.loc[len(elo_rating)] = [time, elo_rating_inicial]
        print('Time adicionado ao arquivo')
        #salvando o arquivo
        elo_rating.to_csv('EloRating.csv', index=False)
        print('Arquivo salvo')
        return False



def lista_times(): #função para listar os times
    elo_rating = Arquivo('EloRating.csv').lendo_arquivo()
    #printando os times
    print('Times:')
    for time in elo_rating['Time'].values:
        print(time)
