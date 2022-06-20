# Elo-Rating-System
## Skil Training
Foram colocadas em praticas skill de classes, Dataframes
## Funcionamento
### Main
No main é apresentado ao usuário um menu onde o usuário escolhe se quer criar um arquivo csv para o funcionamento do programa, caso ele já tenha criado, ele pode escolher listar os times contidos no arquivo, adicionar time ao arquivo, calcular a probabilidade de vitória entre dois times e atualizar o elo dos times.

### Criação de arquivo
Caso o usuário opte por criar um arquivo, será gerado um arquivo com o nome padrão EloRating.csv que servirá de base para o funcionamento do programa.

### Listar Times
Caso o usuário escolha a opção de listar os times, o programa listara todos os times disponíveis no arquivo.

### Adicionar Times
Caso o usuário escolha adicionar um time a lista, o programa pedirá para que seja inserido o nome do time, então irá ser feito uma verificação no arquivo, para analisar se o time informado pelo usuário, já está na base de dados, caso já esteja o time não será adicionado, caso não haja o time informado, o time será adicionado ao arquivo padrão que é utilizado no programa com um Elo inicial padrão de 1500.

### Calcular probabilidade de vitoria
Listará os times disponíveis ao usuário, e pedirá para que seja informado o nome de dois times, será feito uma verificação para confirmar se o time está disponível, se não estiver o time é adicionado com o Elo padrão. Após isso será feito o cálculo da probabilidade de vitória com base nos elos disponíveis.

### Atualizar o Elo do Time
Será pedido ao usuário o nome de dois times e o vencedor da partida, será feita a verificação, após a verificação, será calculado um novo elo para os times e retornará para o usuário qual foi a mudança do elo das equipes.
