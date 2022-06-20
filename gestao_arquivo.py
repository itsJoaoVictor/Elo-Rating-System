import pandas as pd
import numpy as np


#class para criar um arquivo csv via pandas
class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.arquivo = pd.DataFrame({'Time': [], 'Elo Rating': []})
        
    def criar_arquivo(self):
        self.arquivo.to_csv(self.nome_arquivo, index=False)
    
    def lendo_arquivo(self):
        self.arquivo = pd.read_csv(self.nome_arquivo)
        return self.arquivo
    
