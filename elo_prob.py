from auxiliar import checkTeam, lista_times
from gestao_arquivo import Arquivo

#importando sistema de Elo Rating


class EloProb: #classe para calcular a probabilidade de vitoria
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
    
    def prob(self):
        #abrir o arquivo csv de Elo Rating pelo nome
        elo_rating = Arquivo('EloRating.csv').lendo_arquivo()
        #pegando o Elo Rating dos times
        elo_time1 = elo_rating[elo_rating['Time'] == self.time1]['Elo Rating'].values[0]
        elo_time2 = elo_rating[elo_rating['Time'] == self.time2]['Elo Rating'].values[0]
        #calculando a probabilidade de vitória
        prob_time1 = 1 / (1 + 10**((elo_time2 - elo_time1) / 400))
        prob_time2 = 1 / (1 + 10**((elo_time1 - elo_time2) / 400))
        #retornando a probabilidade de vitória
        return prob_time1, prob_time2
    
    @property
    def prob_time1(self):
        return self.prob()[0]
    
    @property
    def prob_time2(self):
        return self.prob()[1]
    
    def __str__(self) -> str:
        #retornando a probabilidade de vitória em formato de string
        return 'Probabilidade de vitória do time {}: {:.2f}%\nProbabilidade de vitória do time {}: {:.2f}%'.format(self.time1, self.prob_time1 * 100, self.time2, self.prob_time2 * 100)