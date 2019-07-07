# -*- coding: utf-8 -*-
print("Seja bem vindo(a) ao um teste vocacional.")

print("Qual é o seu nome?")
nome_do_participante = input("Resposta: ")

print("Oi," +  nome_do_participante +   " então vamos começar as perguntas, para conhecer um pouco mais sobre você.")

linguística=0
logística=0
musical=0
visual_espacial=0
interpessoal=0
intrapessoal=0
corpóreo_cinestésica=0

print("Você aprende facilmente com livros e textos diversos? ")
resposta = (input("Responda sim ou não: ")).upper()
if resposta == "SIM" or resposta == "S":
    linguística+=1
    print("ok")
elif resposta == "NÃO" or resposta == "N":
    print("ok")
else:
    print("Responde direitoooo")

print("Você prefere ler um livro de contos a assistir um filme? ")
ler = (input("Responda sim ou não: ")).upper()
if filme == "SIM" or filme == "S": 
    linguística+=1
    print("ok")
elif filme == "NÃO" or filme == "N":
    print("ok")
else:
    print("Responde direitoooo")

print("Você gosta de escrever nas horas vagas? ")
gosta = (input("Responda sim ou não: ")).upper()
if gosta == "SIM" or gosta == "S":
     linguística+=1  
     print("ok")
elif gosta == "NÃO" or gosta == "N":
    print("ok")
else:
    print("Responde direitoooo")


print("Você tem facilidade com cálculos? ")
facilidade = (input("Responda sim ou não: ")).upper()
if facilidade == "SIM" or facilidade == "S":
    logística+=1
    print("ok")
elif facilidade == "NÃO" or facilidade == "N": 
    print("ok")
else:
    print("Responde direitoooo")
    
print("Para você é importante que existam regras e sempre o uso da lógica? ")
regras = (input("Responda sim ou não: ")).upper()
if regras == "SIM" or regras == "S":
  logística+=1
  print("ok")
elif regras == "NÃO" or regras == "N": 
    print("ok")
else:
    print("Responde direitoooo")

print("Você gosta de exatas? ")
exatas = (input("Responda sim ou não: ")).upper() 
if exatas == "SIM" or exatas == "S":
    logística+=1   
    print("ok")
elif exatas == "NÃO" or exatas == "N": 
    print("ok")
else:
    print("Responde direitoooo")

 
print("Você gosta/sabe tocar indtrumentos? ")
sabe = (input("Responda sim ou não: ")).upper()
if sabe == "SIM" or sabe == "S":
    musical+=1    
    print("ok")
elif sabe == "NÃO" or sabe == "NÃO":
    print("ok")
else:
    print("Responde direitoooo")

print("Você indentifica basicamente tudo que acontece,ao seu redor pelos sons que ouve? ")
basicamente = (input("Resonda sim ou não: ")).upper()
if basicamente == "SIM" or basicamente == "S":
    musical+=1   
    print("ok")
elif basicamente == "NÃO" or basicamente == "N":
    print("ok")
else:
    print("Responde direitoooo")
    
print("É mais importante o tom da voz da pessoa do que, o que ela diz? ")
tom = (input("Responda sim ou não: ")).upper()
if tom == "SIM" or tom == "S":
    musical+=1    
    print("ok")
elif tom == "NÃO" or tom == "N":
    print("ok")
else:
    print("Responde direitoooo")


print("Você cria em seus pensamentos imagens muito nítidas, como:pinturas (você tem facilidade em vizualiza-lás)? ")
imagens = (input("Responda sim ou não: ")).upper()
if imagens == "SIM" or imagens == "S":
    visual_espacial+=1     
    print("ok")
elif imagens == "NÃO" or imagens == "N":
    print("ok")
else:
    print("Responde direitoooo")

perguntas.append("Você tem boa memória para trivialidades? ")
memória = (input("Responda sim ou não: ")).upper()
if memória == "SIM" or memória == "S":
    visual_espacial+=1   
    print("ok")
elif memória == "NÃO" or memória == "N":
    print("ok") 
else:
    print("Responde direitoooo ")

perguntas.append("Você lê com facilidade mapas, esquemas, diagramas, gráficos? ")
mapas = (input("Responda sim ou não: ")).upper()
if mapas == "SIM" or mapas == "S": 
    visual_espacial+=1    
    print("ok")
elif mapas == "NÃO" or mapas == "N":
    print("ok")
else:
    print("Responde direitoooo")
    
print("Você respeita muito as opiniões, objetivos, valores, religiões das pessoas? ")
valores = (input("Responda sim ou não: ")).upper()
if valores == "SIM" or valores == "S":
    interpessoal+=1   
    print("ok")
elif valores == "NÃO" or valores == "N":
    print("ok")
else:
    print("Responde direitoooo")

print("Você gosta da dinâmica de trabalhar em grupo? ")
dinâmica = (input("Responda sim ou não: ")).upper()
if dinâmica == "SIM" or dinâmica == "S":
    interpessoal+=1    
    print("ok")
elif dinâmica == "NÃO" or dinâmica == "N": 
    print("ok")
else:
    print("Responde direitoooo") 

print("Você tem facilidade em resoluções de conflitos? ")
facilidades = (input("Responda sim ou não: ")).upper()
if facilidades == "SIM" or facilidades == "S": 
    interpessoal+=1    
    print("ok")
elif facilidades == "NÃO" or facilidades == "N":
    print("ok")
else:
    print("Responde direitoooo")

print("Você gosta/tem facilidade em locomoção/articular seu corpo? ")
locomoção = (input("Responda sim ou não ")).upper()
if locomoção == "SIM" or locomoção == "S":
    corporéo_cinestésica+=1
    print("ok")
elif locomoção == "NÃO" or locomoção == "N":
    print("ok")
else:
    print("Responde direitoooo")
    

print("Você considera o seu corpo como uma ferramenta? ")
corpo = (input("Responda sim ou não: ")).upper()
if corpo == "SIM" or corpo == "S":
    corpóreo_cinestésica+=1
    print("ok")
elif corpo == "NÃO" or corpo == "N":
    print("ok")
else:
    print("Responde direitoooo")

print("Você tem intuição desenvolvida, embora sempre valorizada? ")
intuição = (input("Responda sim ou não: ")).upper()
if intuição == "SIM" or intuição == "S":
    intrapessoal+=1
    print("ok")
elif intuição == "NÃO" or intuição == "N": 
    print("ok")
else:
    print("Responde direitoooo")
    
    
print("As pessoas sempre te pedem ajuda por você ter otimos conselhos? ")
pedem = (input("Responda sim ou não: ")).upper()
if pedem == "SIM" or pedem == "S":
    intrapessoal+=1  
    print("ok")
elif pedem == "NÃO" or pedem == "N":
    print("ok")
else: 
    print("Responde direitoooo")


if linguística == 3:
    print("A palavra é o fundamental. Quem tem esse tipo de perfil tem talento com as linguagens escritas e faladas, seja para compreender ou para se expressar; próprios de redatores, professores, conferencistas, fonologia etc...")

elif logística == 3:
     print("Talento para o raciocínio, a investigação caracterizado pela facilidade em lidar com os números; pode ser um engenheiro, contador, matemático etc...")

elif visual_espacial == 3: 
     print(" Coisa de quem sabe lidar com a imagem seja, para docodificá-la rapidamente, seja para conseguir vizualizá-la mesmo que não esteja impressa; próprio de arquitetos,geologo, artes, pintores, desenhista,cinema etc...")

elif musical == 3:   
     print("Tem facilidade para identificar sons. Pode ser um talento musical, engenheiro de som; é como se a pessoa exergasse através do som.")


elif copóreo_cinestésica == 2:                    
     print("O corpo é a ferramenta,o instrumento,ou seja, o contato fisíco é básico. O que vale para atores, atletas, dançarinos e para mêcanicos, que usam a habilidade para fazer consertos. Tudo que envolve o corpo.")

elif interpessoal == 3:
     print(" É bom em se relacionar com as pessoas conhece bem o outro e sabe como tirar de cada um o que precisa. Características de Líderes, administradores, relações públicas.")

else:
    print("É o tipo de pessoa que se conhece muito bem (seus limites e possibilidades) tendo capacidade de automotivação. Reservada, ela também é considerada um bom ouvinte próprios de piscologos, gurus e filósofos.")
