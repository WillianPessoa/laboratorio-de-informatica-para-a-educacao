# -*- coding: utf-8 -*-
# Importando a função glob para pegar o nome dos arquivos da pasta gif
from glob import glob

# Importando modulo para exibir gifs
from giphy import showGif
from giphy import showImage

# Importando função para gerar ínteiros randômicos
from random import randint

## Criando lista de perguntas (dicionários)
lista_de_perguntas = []
pontuação = {"humanas": 0, "exatas": 0}

# Pergunta 1
pergunta = dict()
pergunta["pergunta"]="Você prefere um exercício que envolva muitos calculos em vez de fazer uma redação utilizando muitas linhas?"
pergunta["alternativas"]=["Sim",
                          "Não"]
pergunta["correta"] = "a"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 2
pergunta = dict()
pergunta["pergunta"] = "Cotuma se deixar levar pela razão ou emoção?"
pergunta["alternativas"] = ["Razão", "Emoção"]
pergunta["correta"] = "b"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 3
pergunta = dict()
pergunta["pergunta"] = "Um pedreiro diz: Se eu tivesse dois tijolos a mais, o dobro deste número seria 100. Quantos tijolos ele tem?"
pergunta["alternativas"] = ["52", "48", "42", "50", "44"]
pergunta["correta"] = "b"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)


# Pergunta 4
pergunta = dict()
pergunta["pergunta"] = "Consegue dizer a idade de alguém contando a partir do ano em que ela nasceu?"
pergunta["alternativas"] = ["Sim","Não"]
pergunta["correta"] = "b"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 5
pergunta = dict()
pergunta["pergunta"] = "O que você sente mais necessidade de usar?"
pergunta["alternativas"] = ["Calculadora", "Dicionário"]
pergunta["correta"] = "a"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 6
pergunta = dict()
pergunta["pergunta"] = "Quais os nomes dos autores das respectivas obras: 'Quincas Borba' e 'Ou isto ou aquilo"
pergunta["alternativas"] = ["Machado de Assis e Cecilia Meirelles",
                             "Machado de Assis e Clarice Linspector",
                             "José de Alencar e Fernando Pessoa",
                             "Eduardo Spohr e Cecilia Meirelles"]
pergunta["correta"] = "a"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 7
pergunta = dict()
pergunta["pergunta"] = "A soma dos quadrados dos catetos é igual ao quadrado da:"
pergunta["alternativas"] = ["Hiputanosa", "Hipotenusa", "Hupotenosa", "Haputonesa"]
pergunta["correta"] = "a"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 8
pergunta = dict()
pergunta["pergunta"] = "Se atrapalha nos múltiplos de nove?"
pergunta["alternativas"] = ["Sim", "Não"]
pergunta["correta"] = "b"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 9
pergunta = dict()
pergunta["pergunta"] = "Eram uma forma de administração do território colonial português na América."
pergunta["alternativas"] = ["Capitais Hereditárias",
                             "Capitanis Heterogênea",
                             "Capitanias Hereditárias",
                             "Capitais Heterogêneas"]
pergunta["correta"] = "c"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 10
pergunta = dict()
pergunta["pergunta"] = "Se três gatos matam três ratos em três minutos, quanto tempo cem gatos levariam para matar cem ratos?"
pergunta["alternativas"] = ["Cem minutos" , "3 minutos", "30 minutos" ,"100 minutos"]
pergunta["correta"] = "b"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 11
pergunta = dict()
pergunta["pergunta"] = "O que é sociologia?"
pergunta["alternativas"] = ["Ciência que estuda os grupos, sua organização e sua influência sobre a vida dos indivíduos.",
         "Ciência que estuda como os homens evoluíram com o tempo."]
pergunta["correta"] = "a"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 12
pergunta = dict()
pergunta["pergunta"] = "Em uma igreja havia 4 velas. Entraram 2 ladrões e cada um levou uma vela. Quantas velas ficaram?" 
pergunta["alternativas"] = ["6", "2", "4", "1"]
pergunta["correta"] = "a"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 13
pergunta = dict()
pergunta["pergunta"] = "Qual era a maior montanha do mundo antes do Monte Everest ser descoberto?"
pergunta["alternativas"] = ["Everest",
                           "Makalu",
                           "Everst",
                           "Mackalu"]
pergunta["correta"] = "a"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 14
pergunta = dict()
pergunta["pergunta"] = "O Triplo da idade de Fernanda diminuido de 5 é igual a 40. Qual a idade de Fernanda?"
pergunta ["alternativas"] = ["x=16", "x=6", "x=8", "x=15"]
pergunta["correta"] = "d"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 15
pergunta = dict()
pergunta["pergunta"] = "Qual é o maior bloco econômico do mundo?" 
pergunta["alternativas"] = ["Mercosul",
                             "ALCA",
                             "União Européia",
                             "NAFTA"]                             
pergunta["correta"] = "c"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 16
pergunta = dict()
pergunta["pergunta"] = "2x-7=3. Qual é o valor de x?"
pergunta["alternativas"] = ["3", "5", "6", "4"]
pergunta["correta"] = "b"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 17
pergunta = dict()
pergunta["pergunta"] = "Cidadania é um conceito:"
pergunta["alternativas"] = ["Que pressupõe um conjunto de direitos e deveres.",
                           "Que pressuõe abundantes conjuntos de direitos."]                      
pergunta["correta"] = "a"
pergunta["a favor"] ="humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 18
pergunta = dict()
pergunta["pergunta"] = "Quantos meses do ano possuem 30 dias?"
pergunta["alternativas"] = ["11", "5", "12", "4"]
pergunta["correta"] = "a"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Pergunta 19
pergunta = dict()
pergunta["pergunta"] = "A Revolução Indústrial possuía:"
pergunta["alternativas"] = ["Mão de obra em abundância e altos salários.", "Pouca mão de obra e burguesia indústrial.", "Mercado consumidor e mão de obra em abundância."]
pergunta["correta"] = "c"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergunta 20
pergunta = dict()
pergunta["pergunta"] = "Considere em móvel regido pela função horária do movimento retilíneo, S=15+2t. Qual a posição inicial?"
pergunta["alternativas"] = ["2m/s", "7,5m", "15m"]
pergunta["correta"] = "c"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)
        
 # Pergunta 21
pergunta = dict()
pergunta["pergunta"] = "Classifique a seguinte frase: E ELE RIU FROUXAMENTE UM RISO SEM ALEGRIA."
pergunta["alternativas"] = ["Metáfora",
                           "Antítese",
                           "Eufemismo",
                           "Pleonasmo"]
pergunta["correta"] = "d"
pergunta["a favor"] = "humanas"
lista_de_perguntas.append(pergunta)

# Pergutas 22
pergunta = dict()
pergunta["pergunta"] = "Mariana tem 18 anos. Sua irmã mais velha Melissa tem o triplo de sua idade. Quantos anos tem melissa?"
pergunta["alternativas"] = ["24", "36","42", "54", "56"]
pergunta["correta"] = "d"
pergunta["a favor"] = "exatas"
lista_de_perguntas.append(pergunta)

# Gifs a serem exibidos
gif_acertos = glob("Gifs/a*.gif")
gif_erros = glob("Gifs/e*.gif")
tempo = 3

# Mostrar capa
showImage("capa.jpg")

# Exibe as perguntas
for i, item in enumerate(lista_de_perguntas):
    
    # Exibe uma pergunta
    print("{}. {}\n".format(i+1, item["pergunta"]))
    
    # Exibe as alternativas
    for j,alt in enumerate(item["alternativas"]):
        print("{}) {}".format(chr(97+ j), alt))
    print()
    
    # Pegando a resposta
    resposta = input("Qual é a alternativa correta? ").lower()

    # Se o usuário acertou
    if item["correta"] == resposta:
            # Pontua a favor
            pontuação[item["a favor"]] += 1
            #Exibe gif de acerto
            showGif(gif_acertos[randint(0, len(gif_acertos)-1)], tempo)
    else:
            # Exibe gif de erro
            showGif(gif_erros[randint(0, len(gif_erros)-1)], tempo)

# Avaliando os acertos
if pontuação["humanas"] > pontuação ["exatas"]:
    print("Seu coração bate pelos números!")
    print("Exatidão, razão e precisão, este é o seu lema!")
    print("Não deixe de estudar o que gosta para agradar outra pessoa.")

elif pontuação["humanas"] == pontuação ["exatas"]:
    print("Você é @ privilegiad@!")
    print("Abençoad@ por Deus!")
    print("Indefeituoso!")
    
else:
    print("Com toda certeza você é de humanas!")
    print("Não deixe de estudar o que gosta para agradar outra pessoa, seu coração irá cobra depois.\n")

    
