from auxiliar import checkTeam, lista_times
from elo_prob import EloProb
from gestao_arquivo import Arquivo



#classe para atualizar o Elo Rating de um time da lista
class EloAtualizacao:
    
    def __init__(self, time1, time2, resultado):
        self.time1 = time1
        self.time2 = time2
        self.resultado = resultado
    
    def atualizar(self):
        #importando sistema de Elo Rating
        elo_rating = Arquivo('EloRating.csv').lendo_arquivo()
        #calculando a probabilidade de vitória
        prob_time1, prob_time2 = EloProb(self.time1, self.time2).prob()
        #atualizando o Elo Rating
        #se o time 1 venceu
        if self.resultado == self.time1:
            #pegando o Elo Rating dos times
            elo_time1 = elo_rating[elo_rating['Time'] == self.time1]['Elo Rating'].values[0]
            elo_time2 = elo_rating[elo_rating['Time'] == self.time2]['Elo Rating'].values[0]
            #calculando o novo Elo Rating
            elo_time1_novo = elo_time1 + 32 * (1 - prob_time1 / 100)
            elo_time2_novo = elo_time2 + 32 * (0 - prob_time2 / 100)
            #atualizando o Elo Rating
            elo_rating.loc[elo_rating['Time'] == self.time1, 'Elo Rating'] = elo_time1_novo
            elo_rating.loc[elo_rating['Time'] == self.time2, 'Elo Rating'] = elo_time2_novo
        #se o time 2 venceu
        elif self.resultado == self.time2:
            #pegando o Elo Rating dos times
            elo_time1 = elo_rating[elo_rating['Time'] == self.time1]['Elo Rating'].values[0]
            elo_time2 = elo_rating[elo_rating['Time'] == self.time2]['Elo Rating'].values[0]
            #calculando o novo Elo Rating
            elo_time1_novo = elo_time1 + 32 * (0 - prob_time1 / 100)
            elo_time2_novo = elo_time2 + 32 * (1 - prob_time2 / 100)
            #atualizando o Elo Rating
            elo_rating.loc[elo_rating['Time'] == self.time1, 'Elo Rating'] = elo_time1_novo
            elo_rating.loc[elo_rating['Time'] == self.time2, 'Elo Rating'] = elo_time2_novo
        #se empate
        elif self.resultado == 'empate':
            #pegando o Elo Rating dos times
            elo_time1 = elo_rating[elo_rating['Time'] == self.time1]['Elo Rating'].values[0]
            elo_time2 = elo_rating[elo_rating['Time'] == self.time2]['Elo Rating'].values[0]
            #calculando o novo Elo Rating
            elo_time1_novo = elo_time1 + 32 * (0.5 - prob_time1 / 100)
            elo_time2_novo = elo_time2 + 32 * (0.5 - prob_time2 / 100)
            #atualizando o Elo Rating
            elo_rating.loc[elo_rating['Time'] == self.time1, 'Elo Rating'] = elo_time1_novo
            elo_rating.loc[elo_rating['Time'] == self.time2, 'Elo Rating'] = elo_time2_novo
        #salvando o arquivo
        elo_rating.to_csv('EloRating.csv', index=False)
        #printando o novo Elo Rating formatado
        print('Elo Rating atualizado:')
        print(f' O time {self.time1} teve o ELo Rating atualizado de {elo_time1:.2f} para {elo_time1_novo:.2f}')
        print(f' O time {self.time2} teve o ELo Rating atualizado de {elo_time2:.2f} para {elo_time2_novo:.2f}')
        
        
