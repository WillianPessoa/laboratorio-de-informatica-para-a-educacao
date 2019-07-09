# Pergunta o nome do Jogador
nome = input("Oi, qual o seu nome?\n > ").capitalize()

# Mensagem que começa o quiz!
print(f'Show do Milhão\n{nome}, vamos começar!!\n')

# Lista das alternativas certas e o valor de cada questão
certas=['2','2','2','2','4','1','2','3','3','4','4','3','3','4','2','3','2','4','2','2','1']
valor_quest=[1_000,9_000, 10_000, 20_000, 20_000, 20_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 70_000, 80_000, 50_000, 60_000,65_000, 75_000, 85_000, 75_000, 90_000]

# Abrindo o arquivo feito no bloco de notas no modo leitura
arquivo = open("perguntas.txt", 'r')

dinheiro = 0

# Iteramos (percorremos) a lista criada pelo range, 21 vezes
# i -> recebe o indice atual 
for i in range(21):

    # Criamos condicionais para indicar os niveis de dificuldade do quiz
    if i == 0:
        print("="*80+'\n', 'Nivel-Fácil:\n')
    if i == 7:
        print("="*80+'\n', 'Nivel-Médio\n')
    if i == 14:
        print("="*80+'\n', 'Nivel-Dificil\n')

    #Lê 5 linhas do arquivo
    for _ in range(5):
        print(arquivo.readline(), end='')

    resposta = input("Resposta: ")

    #Condicional para verificar se o usuário acertou a pergunta
    if resposta == certas[i]:
        dinheiro += valor_quest[i]
        print("A resposta está correta!\n")
    else:
        print(f'Resposta incorreta! A resposta correta era {certas[i]}.\n')
        
print (f'Parabénssss, {nome}!!!Você vai levar {dinheiro:,} para casa.')
