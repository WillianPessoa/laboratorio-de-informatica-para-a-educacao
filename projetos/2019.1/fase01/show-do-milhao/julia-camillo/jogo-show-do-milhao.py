
#PROJETO SHOW DO MILHAO

def respostasn():
    aux= input("Resposta: ")
    while aux != "s" and aux != "n":
            print("\n•Sua resposta deve ser [s] ou [n]!")
            aux = input ("\nResposta: ")
    return aux

#Perguntas fáceis

print("SHOW DO :corn:! :D")

print("\nQuer um tutorial? Responda com [s] ou [n].\n")

tutorial = respostasn()
if tutorial == "s":
 print("\n\nSobre o jogo: \n\nEsse é um jogo de perguntas e respostas com um prêmio final de 1 milhão de reais (se alguém bancar, realmente será).")
 print("\n=>Nesse jogo você você responderá a 24 perguntas. Sendo: \n•De 1 à 5: Nível Ultrafácil \n•De 6 à 11: Nível Fácil \n•De 12 à 17: Nível Médio \n•De 18 à 23: Nível Difícil \n•24: Pergunta de 1 milhão")
 print("\n=>Acertos, Erros e Desistências: \nObs: os valores são referentes a quanto você receberá no caso de acerto, erro ou desistência das perguntas nas posições destacadas: ")
 print("\n-Acertos: \n\n•Ao acertar a primeira você adicionará $500 à sua conta.•Apartir da 2ª, serão acumulados 100$ a cada acerto, até a 5ª pergunta. \n•Apartir da 6ª serão acumulados $1000 a cada acerto, até a 11ª pergunta. \n•Apartir da 12ª serão acumulados $10.000 a cada acerto até a 17ª. \n•Apartir da 18ª serão acumulados $100.000 a cada acerto, até a 23ª. \n•A última pergunta (24) vale 1 milhão.")
 print("\n\n-Erros:  \n\n•1ª = $0 \n•2ª até 7ª = Inicia-se com $250 e é acumulade $50 a cada pergunta correta\n•8ª até 12ª = Inicia-se com $1000 e é acumulado $500 a cada pergunta correta. \n•13ª até 19ª =  Inicia-se com $5.000, e é acumulado $5.000 a cada pergunta correta. \n•20ª até 23ª = Inicia-se com $50.000, e é acumulado $50.000 a cada pergunta correta. \n•24ª = $0")
 print("\n\n-Desistências: \n\n•1ª = 0 \n•2ª até 6ª = Inicia-se com $500 e é acumulado $100 a cada pergunta correta. \n•7ª até 12ª = Inicia-se com $1000, e é acumulado $1000 a cada pergunta correta. \n•13ª até 18ª = Inicia-se com $10.000, e é acumulado $10.000 a cada pergunta correta. \n•19ª até 23ª = Inicia-se com $100.000, e é acumulado $100.00 a cada pergunta correta. \n•24ª = $0")
 print("\n\n=>Dicas: \n\n•Convidados - Três estudantes de diversas faculdades dão suas respostas à pergunta. Cabe a você confiar ou não. \n\n•Placas - Uma pequena plateia levanta placas numeradas, referentes à alternativa correta. Por exemplo, para a terceira alternativa, levantam a placa de número 3. Cabe a você decidir se concorda com a maioria das alternativas ou não. \n\n•Cartas - Quatro cartas de baralho são viradas e o participante escolhe uma. Se tirar o Rei, nenhuma alternativa errada é eliminada. Ás elimina uma alternativa, 2 elimina duas alternativas e 3 elimina todas as três alternativas erradas, restando apenas a correta. \n\n•Pulos - Você poderá 'pular' a pergunta caso não saiba a resposta. Esse recurso pode ser utilizado até três vezes. \n\nObs: Na pergunta final, que vale o prêmio máximo, nenhuma das ajudas poderá ser usada. Você terá de escolher se responde à pergunta ou para o jogo e sai com R$600 mil.")

import random
p1= "O que cinderela perdeu ao sair do baile do palácio real?"
a1= ["a)Bolsa", "b)Luva", "c)Carteira de Motorista", "d)Sapato de cristal"]
r= "d"

p2= "Um analgésico é um agente para:"
a2= ["a)Tratamento do intestino", "b)Alívio de estresse", "c)Alívio da dor","d)Tratamento da caspa"]
r2= "c"

p3= "De que é feito o pé-de-moleque?"
a3= ["a)Amendoim", "b)Castanha", "c)Alcaparra", "d)Abacate"]
r3= "a"

p4= "Quantos anos tem um milênio?"
a4= ["a)100", "b)500", "c)100", "d)1000"]
r4= "d"

p5= "Onde a mãe canguru carrega o filhote?"
a5= ["a)Na orelha", "b)Nas costas", "c)Na boca", "d)Na bolsa"]
r5= "d"

p6= "O que é a morsa?"
a6= ["a)Um réptil", "b)Um mamífero", "c)Um peixe", "d)Um crustáceo"]
r6= "b"

p7= "O que é um croissant?"
a7= ["a)Licor",  "b)Doce", "c)Tempero",  "d)Pão"]
r7= "d"

p8= "O que se joga na neve para ajudar a derretê-la?"
a8= ["a)Açúcar", "b)Orégano", "c)Sal",  "d)Pimenta"]
r8= "c"

p9= "Qual é a cidade do Batman?"
a9= ["a)Gotham City", "b)Metrópolis", "c)Pleasantville", "d)Anytown"]
r9= "a"

p10= "O que a Rapunzel jogava pela janela?"
a10= ["a)Perna", "b)Braço", "c)Família", "d)Trança"]
r10= "d"

p11= "Qual é o coletivo de cães?"
a11= ["a)Matilha", "b)Rebanho",  "c)Cardume", "d)Manada"]
r11= "a"

p12= "Qual é a maior floresta do planeta?"
a12= ["a)Negra", "b)de Sherwood", "c)da Tijuca", "d)Amazônica"]
r12= "d"

p13= "Qual é o santo que só acreditou vendo?"
a13= ["a)Santo Antônio", "b)São Judas Tadeu", "c)São Pedro", "d)São Tomé"]
r13= "d"

p14= "Como é conhecido o jogador Edmundo?"
a14=["a)Tigrão", "b)Gatinho", "c)Animal", "d)Cobra"]
r14= "c"

p15= "Qual animal é o pateta?"
a15= ["a)Cavalo", "b)Burro",  "c)Cachorro", "d)Raposa"]
r15= "c"

p16= 'Em qual parte do corpo humano são implantadas as "pontes de safena"?'
a16 = ["a)Estômago", "b)Intestino",  "c)Pulmão", "d)Coração"]
r16= "d"

p17= 'Quem é conhecido como o "playboy brasileiro"?'
a17= ["a)Joãozinho Trinta", "b)Zeca pagodinho", "c)Chiquinho Scarpa", "d)Chico Buarque"]
r17= "c"

p18= "Quantos centímetros equivalem a um metro?"
a18= ["a)10", "b)100", "c)1000", "d)10000"]
r18= "b"

p19= "Qual é o inseto que transmite a doença de chagas?"
a19= ["a)Abelha", "b)Barata", "c)Barbeiro", "d)Pulga"]
r19= "c"

p20= "Como eram chamados os navios que traziam os escravos para o Brasil?"
a20= ["a)Branqueiros", "b)Pesqueiros", "c)Negreiros", "d)Costeiros"]
r20= "c"

p21= "Qual nome é dado à criança ainda não batizada?"
a21= ["a)Pagão", "b)Anão", "c)Chorão", "d)Cristão"]
r21= "a"

p22= "Como se chama a armação do óculos?"
a22= ["a)Roda", "b)Eixo", "c)Arco", "d)Aro"]
r22= "d"

p62= "Qual ator imortalizou o personagem Zé Bonitinho?"
a62= ["a)Róni Cócegas", "b)Jorge Loredo", "c)Davi Pinheiro", "d)Arnaud Rodrigues"]
r62= "b"

#Médio
p23= "Que imperador pôs fogo em Roma?"
a23= ["a)Trajano", "b)Nero", "c)Brutus", "d)Calígula"]
r23= "b"

p24= "O que é gôndola?"
a24= ["a)Embarcação", "b)Brinquedo", "c)Música", "d)Símbolo"]
r24= "a"

p25= "Como eram chamados os pilotos suicidas da segunda guerra mundial?"
a25= ["a)Camicases", "b)Sashimis", "c)Haraquiris", "d)Sumôs"]
r25= "a"

p26= "Quem foi eleito presidente da África do Sul em 1994?"
a26= ["a)Nelson Piquet", "b)Nelson Mandela", "c)Nelson Ned", "d)John Nelson"]
r26= "b"

p27= "Qual é a moeda oficial da Alemanha?"
a27= ["a)Peso", "b)Marco", "c)Lira", "d)Libra"]
r27= "b"

p28= "Que país europeu tem como atração a trourada?"
a28= ["a)Espanha", "b)Itália", "c)França", "d)Alemanha"]
r28= "a"

p29= "O que os filatelistas colecionam?"
a29= ["a)Quadros", "b)Moedas", "c)Selos", "d)Figurinhas"]
r29= "c"

p30= "Que animais são criados nas pocílgas?"
a30=["a)Camelos", "b)Búfalos", "c)Carneiros", "d)Porcos"]
r30= "d"

p31= "Quem é o parceiro de aventuras de Dom Quixote?"
a31=["a)Sigmund Freud", "b)Guilherme Tell", "c)Sancho Pança", "d)Lancelot"]
r31= "c"

p32= "Como se chama a máquina usada para compactar o asfalto?"
a32=["a)Rolo compressor", "b)Escavadeira", "c)Trator", "d)Pixeiro"]
r32= "a"

p33= "Qual dessas cobras não é venenosa?"
a33=["a)Urutu", "b)Cascavel", "c)Jararaca", "d)Píton"]
r33= "d"

p34= "Camillo é o sobrenome de qual cantor nascido em Brotas?"
a34=["a)Leonardo", "b)Chitãozinho", "c)Daniel", "d)Vinny"]
r34= "c"

#difícil
p35= "Em qual país está localizado o Muro das Lamentações?"
a35=["a)Alemanha", "b)Brasil", "c)Venezuela", "d)Israel"]
r35= "d"

p36= "Em qual Espécie o macho choca os ovos e a fêmea procura alimento?"
a36=["a)Andorinha", "b)Pato Selvagem", "c)Pingüim", "d)Marreco"]
r36= "c"

p37= "Qual presidente brasileiro instituiu o AI-5?"
a37=["a)Costa e Silva", "b)Ernesto Geisel", "c)João Figueiredo", "d)Itamar Franco"]
r37= "a"

p38= "Qual oceano tem o maior volume de água?"
a38=["a)Atlântico", "b)Pacífico", "c)Índico", "d)Ártico"]
r38= "b"

p39="Qual foi o último presidente militar do Brasil?"
a39=["a)Fernando Collor", "b)João Figueiredo", "c)Tancredo Neves", "d)João Goulart"]
r39= "b"

p40= "Qual produto gere guerras e conflitos no século XX?"
a40=["a)Álcool", "b)Petróleo", "c)Ouro", "d)Aço"]
r40= "b"

p41= "Como é chamada a bola de gelo e poeira que orbita em torno do sol?"
a41=["a)Cometa", "b)Meteorito", "c)Camada de Izônio", "d)Estrela D'Alva"]
r41= "a"

p42= "A eletrônica é parte de qual ciência?"
a42=["a)Física", "b)Biologia", "c)Química", "d)Botânica"]
r42= "a"

p43= "Que nome receba a foz de um rio que se abre para o mar?"
a43=["a)Alagado", "b)Manguezal", "c)Pântano", "d)Estuário"]
r43= "d"

p44= 'De quem é a frase: "Penso, logo existo"?'
a44=["a)Platão", "b)Júlio Verne", "c)Aristóteles", "d)René Descartes"]
r44= "d"

p45= 'A quem se atribuiu a frase "Eu sou o Estado"?'
a45= ["a)Luís XIV", "b)Luís XV", "c)Luís XVI", "d)Napoleão Bonaparte"]
r45= "a"

p46= "Qual foi a locomotiva a vapor que trafegou na Estrada de Ferro Mauá em 1854?"
a46=["a)Santa-fé", "b)Loco-Breque", "c)American", "d)Baronesa"]
r46= "d"

p47= "Qual atleta foi desclassificado por uso de doping?"
a47=["a)Mike Powell", "b)Ben Johnson", "c)Carl Lewis", "d)Linford Christie"]
r47= "b"

p48= "Quem escreveu Dom Quixote?"
a48=["a)Espinoza", "b)Miguel de Cervantes", "c)Carlos Conte", "d)Angel Morita"]
r48= "b"

p49="Qual a origem da palavra folclore?"
a49=["a)Holandesa", "b)Inglesa", "c)Francesa", "d)Brasileira"]
r49= "b"

p50= "O que é glicose?"
a50=["a)Aminoácido", "b)Hidrato de Carbono", "c)Lipídio", "d)Proteína"]
r50= "b"

p51= "As Ilhas Malvinas também são chamadas de:"
a51=["a)Stanley", "b)Wedells", "c)Medanosa", "d)Falkland"]
r51= "d"

p52= "Pablo Picasso foi um dos criadores do:"
a52=["a)Cubismo", "b)Surrealismo", "c)Impressionismo", "d)Realismo"]
r52= "a"

p53= "Como se chama o explorador de grutas e cavernas?"
a53=["a)Espeleólogo", "b)Agrostólogo", "c)Psicólogo", "d)Campanólogo"]
r53= "a"

p54= "Como é chamada a gravura impressa sobre pranchas de madeira?"
a54=["a)Materografia", "b)Litografia", "c)Xilografia", "d)Serigrafia"]
r54= "c"

#1mi
p55= "O que significa literalmente Perestroika?"
a55=["a)Conversão", "b)Involução", "c)Reestruturação", "d)Regressão"]
r55= "c"

p56= "O que significa o prefixo exo?"
a56=["a)Dentro de", "b)Debaixo n", "c)Fora de", "d)Atrás de"]
r56= "c"

p57= "Qual foi o metal utilizado na construção do Partenon de Atenas?"
a57=["a)Mármore", "b)Granito", "c)Gesso", "d)Quartzo"]
r57= "a"

p58= "Em que ano foi inaugurada a estáua do Cristo Redentor no Rio de Janeiro?"
a58=["a)1921", "b)1931", "c)1941", "d)1951"]
r58= "b"

p59= "Qual dessas palavras é sinônimo de cabal?"
a59=["a)Baixo", "b)Perfeito", "c)Atrevido", "d)Enfermo"]
r59= "b"

p60= "A baleia está classificada em qual grupo de mamíferos?"
a60=["a)Cetáceos", "b)Felinos", "c)Sirênios", "d)Carnívoros"]
r60=  "a"

p61= "Qual é a maior ilha da Europa?"
a61=["a)Grã-Bretanha", "b)Irlanda", "c)Islândia", "d)Sicília"]
r61= "a"

#==============================
#VARIÁVEIS

pergunta1= [p1, p2, p3, p4, p5, p7, p9, p10, p11, p15, p18, p20, p21, p22] 
alternativa1= [a1, a2, a3, a4, a5, a7, a9, a10, a11, a15, a18, a20, a21, a22]
resposta1 = [r, r2, r3, r4, r5, r7, r9, r10, r11, r15, r18, r20, r21, r22]
x = 0
p=0
quant= 0
prox=0
y= 0
errar2= 0
parar2= 0
acertar2= 1000
dinheru = 400
ajudas = ["1. Convidados", "2. Placas", "3. Cartas", "4. Pular"]
r1 = ""

#==============================
#FUNÇÕES

#pergunta:
def pergunta():
    indice = random.randint(1,len(pergunta1)) - 1
    pergunta_level1 = pergunta1[indice]
    resposta_level1 = resposta1[indice]
    alternativa_level1 = alternativa1[indice]
    pergunta1.pop(indice)
    resposta1.pop(indice)
    alternativa1.pop(indice)
    print("===================================================================")
    print("\n{}ª pergunta){} \n\n{} \n{} \n{} \n{}".format(x, pergunta_level1, alternativa_level1[0], alternativa_level1[1], alternativa_level1[2], alternativa_level1[3]))
    print("")
    return [pergunta_level1,resposta_level1,alternativa_level1]
    
#respostas do usuario
def respostadousuario():
    aux= input("Resposta: ")
    while (aux != "a" and aux != "b" and aux != "c" and aux != "d" and aux != "1" and aux != "2" and aux != "parar" and aux !="3" and aux != "4"):
        print("\n•Sua resposta deve ser uma das alternativas, uma das ajudas ou o que for pedido!")
        aux = input ("\nResposta: ")
    return aux

def respostadasdicas():
    aux= input("Resposta: ")
    while aux != "a" and aux != "b" and aux != "c" and aux != "d" and aux != "parar":
        print("\n•Sua resposta deve ser uma das alternativas, ou o que for pedido!")
        aux = input ("\nResposta: ")
    return aux

def respostacartas():
    aux= input("Resposta: ")
    while aux != "1" and aux != "2" and aux != "3" and aux != "4":
            print("\n•Sua resposta deve ser [1], [2], [3] ou [4]!")
            aux = input ("\nResposta: ")
    return aux


#AJUDAS

#convidados:
	#1
def convidados_level1():
    ajudas.remove("1. Convidados")        
    if resposta_level1== "a":
        lista= ["b", "c", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'a'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'a'."
        lista2= [convidados2, convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "b":
        lista= ["a", "c", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'b'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'b'."
        lista2= [convidados2, convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "c":
        lista= ["a", "b", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'c'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'c'."
        lista2= [convidados2, convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "d":
        lista= ["a", "c", "b"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'd'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'd'."
        lista2= [convidados2, convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
    return r1
#2
def convidados_level2():
    ajudas.remove("1. Convidados")        
    if resposta_level1== "a":
        lista= ["b", "c", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'a'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'a'."
        lista2= [convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "b":
        lista= ["a", "c", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'b'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'b'."
        lista2= [convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "c":
        lista= ["a", "b", "d"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'c'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'c'."
        lista2= [convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "d":
        lista= ["a", "c", "b"]
        letra1= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'd'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votaram em 'd'."
        lista2= [convidados2, convidados1]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
    return r1
#3
def convidados_level3():
    ajudas.remove("1. Convidados")        
    if resposta_level1== "a":
        lista= ["b", "c", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'a'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'a'."
        convidados3= "Dois dos convidados votaram em 'a'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados2, convidados1, convidados1, convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "b":
        lista= ["a", "c", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'b'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'b'."
        convidados3= "Dois dos convidados votaram em 'b'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados2, convidados1, convidados1, convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "c":
        lista= ["a", "b", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'c'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'c'."
        convidados3= "Dois dos convidados votaram em 'c'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados2, convidados1, convidados1, convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "d":
        lista= ["a", "c", "b"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'd'. Um convidado votou em '{}'".format(letra1)
        convidados2= "Quatro dos convidados votou em 'd'."
        convidados3= "Dois dos convidados votaram em 'd'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados2, convidados1, convidados1, convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
    return r1
#4
def convidados_level4():
    ajudas.remove("1. Convidados")        
    if resposta_level1== "a":
        lista= ["b", "c", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'a'. Um convidado votou em '{}'".format(letra1)
        convidados3= "Dois dos convidados votaram em 'a'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "b":
        lista= ["a", "c", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'b'. Um convidado votou em '{}'".format(letra1)
        convidados3= "Dois dos convidados votaram em 'b'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "c":
        lista= ["a", "b", "d"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'c'. Um convidado votou em '{}'".format(letra1)
        convidados3= "Dois dos convidados votaram em 'c'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
        
    if resposta_level1== "d":
        lista= ["a", "c", "b"]
        letra1= random.choice(lista)
        lista.remove(letra1)
        letra2= random.choice(lista)
        convidados1 = "Três dos convidados votaram em 'd'. Um convidado votou em '{}'".format(letra1)
        convidados3= "Dois dos convidados votaram em 'd'. Um convidado votou em '{}', e um convidado votou em '{}'.".format(letra1, letra2)
        lista2= [convidados1, convidados3]
        resp= random.choice(lista2)
        print(resp)
        r1 = respostadasdicas()
        print("")
    return r1
    
#placas:
def placas():
    ajudas.remove("2. Placas")
    print("•{}% votou em '{}'".format(random.randint(90,100), resposta_level1))
    r1 = respostadasdicas()
    print("")
    while r1 == "2":
        print("•Você já usou essa função. Não pode usá-la novamente.")
        r1 = respostadasdicas()
        print("")
    return r1
    
#cartas:
def cartas():
    try:
        ajudas.remove("3. Cartas")
        import random
        rei= "Rei"
        ás = "Ás"
        dois = "2"
        tres = "3"
        cartas = [rei, ás, dois, tres]
        carta = random.choice(cartas)
        print("•Escolha uma das cartas: 1ª, 2ª, 3ª, 4ª \nResponda sem o 'ª'\n")
        r1 = respostacartas()
        print("")
        
        if carta == rei: #rei
            print("•A Carta escolhida foi o Rei. Que pena! Nenhuma alternativa será removida :/.\n")
            r1 = respostadasdicas()
            print("")
            
        elif carta == ás: #ás
            print("•A carta escolhida foi o Ás. Uma alternativa errada foi removida: \n")
            if resposta_level1== "a":
                lista= [1, 2, 3]
                indice= random.choice(lista)
                lista.remove(indice)
                indice2= random.choice(lista)
                alternativas= [alternativa_level1[0], alternativa_level1[indice], alternativa_level1[indice2]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1] + "\n" + alternativas[2])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "b":
                lista= [0, 2, 3]
                indice= random.choice(lista)
                lista.remove(indice)
                indice2= random.choice(lista)
                alternativas= [alternativa_level1[1], alternativa_level1[indice], alternativa_level1[indice2]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1] + "\n" + alternativas[2])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "c":
                lista= [0, 1, 3]
                indice= random.choice(lista)
                lista.remove(indice)
                indice2= random.choice(lista)
                alternativas= [alternativa_level1[2], alternativa_level1[indice], alternativa_level1[indice2]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1] + "\n" + alternativas[2])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "d":
                lista= [0, 1, 2]
                indice= random.choice(lista)
                lista.remove(indice)
                indice2= random.choice(lista)
                alternativas= [alternativa_level1[3], alternativa_level1[indice], alternativa_level1[indice2]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1] + "\n" + alternativas[2])
                r1 = respostadasdicas()
                print("")
        
        elif carta == dois: #dois
            print("•A carta escolhida foi o Dois. Duas alternativas erradas foram removidas: \n")
            if resposta_level1== "a":
                lista= [1, 2, 3]
                indice= random.choice(lista)
                alternativas= [alternativa_level1[0], alternativa_level1[indice]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "b":
                lista= [1, 2, 3]
                indice= random.choice(lista)
                alternativas= [alternativa_level1[1], alternativa_level1[indice]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "c":
                lista= [1, 2, 3]
                indice= random.choice(lista)
                alternativas= [alternativa_level1[2], alternativa_level1[indice]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1])
                r1 = respostadasdicas()
                print("")
            if resposta_level1== "d":
                lista= [1, 2, 3]
                indice= random.choice(lista)
                alternativas= [alternativa_level1[3], alternativa_level1[indice]]
                alternativas.sort()
                print(alternativas[0] + "\n"+ alternativas[1])
                r1 = respostadasdicas()
                print("")
            
        elif carta == tres: #tres
            print("•A carta Três foi escolhida. As três alternativas erradas foram removidas.\n")
            if resposta_level1== "a":
                alternativa_level1.pop(1)
                alternativa_level1.pop(1)
                alternativa_level1.pop(1)
                print(alternativa_level1[0])
            if resposta_level1== "b":
                alternativa_level1.pop(0)
                alternativa_level1.pop(1)
                alternativa_level1.pop(2)
                print(alternativa_level1[0])
            if resposta_level1== "c":
                alternativa_level1.pop(0)
                alternativa_level1.pop(0)
                alternativa_level1.pop(1)
                print(alternativa_level1[0])
            if resposta_level1== "d":
                alternativa_level1.pop(0)
                alternativa_level1.pop(0)
                alternativa_level1.pop(0)
                print(alternativa_level1[0])
            print("")
            r1 = respostadasdicas()
            print("")
            if r1 != resposta_level1:
                print("Todas as alternativas erradas foram removidas, você realmente vai fazer isso?")
                r1 = respostadasdicas()
                if r1 != resposta_level1:
                        print("Ok. Se você quer assim, que assim seja.\n")
        return r1
    except:
        while r1 == "3":
                print("\n Você não pode usar mais essa função!")
                r1 = respostadasdicas()
        return r1

#pular:
def pular(p, r1, quant):
    try:
        p+=1
        quant-=1
        if p > 3:
            while r1 == "4":
                print("Você já pulou três vezes. Você não pode usar mais essa função!")
                r1 = respostadasdicas()
                quant += 1
        return [p, r1, quant]
    except:
        while r1 == "4":
            print("Você já pulou três vezes. Você não pode usar mais essa função!")
            r1 = respostadasdicas()
            quant += 1
        return [p, r1, quant]
    
#AÇÕES DAS PERGUNTAS
def acerto(dinheru, prox): #ACERTO
    if x >= 1 and x <= 6:
        dinheru += 100
    if x > 6 and x <=11:
        dinheru += 1000
    if x == 12:
        dinheru = 0
    if x >= 11 and x <=18:
        dinheru += 10000
    if x == 18:
        dinheru = 0
    if x >= 18 and x <= 24:
        dinheru += 100000
    print ("Resposta Correta! Parabéns! Você ganhou $"+ str(dinheru) + ".")
    print("")
    prox +=1
    return [dinheru, prox]
    
def parar(): #PARAR
    if x == 2:
             print("Ok! Você levará para casa $500. Sobre o recebimento, tire satisfações com um dos monitores.")
             print("\nGostaria de saber qual era a resposta correta?")
             r1 = respostasn()
             if r1 == "s":
                print("A resposta correta era '{}'".format(resposta_level1))
    if x == 1:
        print("Ok. Você levará para casa $0.")
        print("\nGostaria de saber qual era a resposta correta?")
        r1 = respostasn()
        if r1 == "s":
            print("A resposta correta era '{}'".format(resposta_level1))
    else:
        print("Ok! Você levará para casa {}$.".format(dinheru))
        print("\nGostaria de saber qual era a resposta correta?")
        r1 = respostasn()
        if r1 == "s":
            print("A resposta correta era '{}'".format(resposta_level1))

def erroa(): #ERRO
    if r1 == 'b' or r1 == 'c' or r1 == 'd':
        if x == 1:
            print("Você errou! \nInfelizmente você não levará nada.")
        else:
            print("Você errou! Você levará ${}.".format(int(parar2/2)))

def errob():
     if r1 == 'a' or r1 == 'c' or r1 == 'd':
        if x == 1:
            print("Você errou! \nInfelizmente você não levará nada.")
        else:
            print("Você errou! Você levará ${}.".format(int(parar2/2)))
                
def erroc():
    if r1 == 'b' or r1 == 'a' or r1 == 'd':
        if x== 1:
            print("Você errou! \nInfelizmente você não levará nada.")
        else:
            print("Você errou! Você levará ${}.".format(int(parar2/2)))

def errod():
    if r1 == 'b' or r1 == 'c' or r1 == 'a':
        if x== 1:
            print("Você errou! \nInfelizmente você não levará nada.")
        else:
            print("Você errou! Você levará ${}.".format(int(parar2/2)))

#DIÁLOGO COM O USUÁRIO

def dialogo2(x,errar2, parar2, acertar2):
    
    if x == 6:
        errar2= 450
        parar2= 900
        acertar2= 1000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 7:
        errar2= 500
        parar2= 1000
        acertar2= 2000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x > 7 and x < 11:
        errar2+= 500
        parar2+= 1000
        acertar2+= 1000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 11:
        errar2= 2500
        parar2= 5000
        acertar2= 6000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 12:
        errar2= 3000
        parar2= 6000
        acertar2 = 10000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 13:
        errar2= 5000
        parar2= 10000
        acertar2= 20000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x > 13 and  x < 18:
        errar2+= 5000
        parar2+= 10000
        acertar2+= 10000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 18:
        acertar2 = 100000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 19:
        errar2= 50000
        parar2= 100000
        acertar2= 200000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x > 19 and x <= 23:
        if r1 != "4":
            errar2+= 50000
            parar2+= 100000
            acertar2+= 100000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    if x == 24:
        errar2 = 300
        parar2= 600000
        acertar2= 1000000
        print("•Errar: ${}.".format(errar2))
        print("•Parar: ${}.".format(parar2))
        print("•Acertar: ${}.".format(acertar2))
    return [errar2, parar2, acertar2]


print ("\n\nIniciar!")
print("")

#===============================
#PERGUNTAS LEVEL 1

while quant < 5:
    quant += 1
    y = quant
    x = quant
    lista = pergunta()
    pergunta_level1 = lista[0];
    resposta_level1 = lista[1]
    alternativa_level1 = lista[2];
    
    #==============================
    #DIÁLOGO COM O USUÁRIO 1
        
    if x == 1:
        print("•Se você errar agora não levará nada.")
        print("•Acertar: $500.")
        parar2= 0
    elif x == 2:
        print("•Errar: $250.")
        print("•Parar: $500.")
        print("•Acertar: $600.")
        parar2= 500
    elif x == 3:
        print("•Errar: $300.")
        print("•Parar: $600.")
        print("•Acertar: $700.")
        parar2= 600
    elif x == 4:
        print("•Errar: $350.")
        print("•Parar: $700.")
        print("•Acertar: $800.")
        parar2= 700
    elif x == 5:
        print("•Errar: $400.")
        print("•Parar: $800.")
        print("•Acertar: $900.")
        parar2= 800
    elif x!=1:
        print("Para parar digite: parar")

    print("Para parar digite: parar")
    print ("\nAjudas: " + str(ajudas))
    print("")

    r1 = respostadousuario()
    print("")
    
    #==============================
    #AJUDAS 1
    
    #Convidados:
    if r1 == "1":
        r1 = convidados_level1()       
            
    #Placas:
    elif r1 == "2":
        r1 = placas()
                
    #Cartas:
    elif r1 == "3":
        r1 = cartas()

        #Pular:
    elif r1 == "4":
        lista = pular(p, r1, quant)
        p = lista[0]
        r1 = lista[1]
        quant = lista[2]
        if p == 3:
            ajudas.remove("4. Pular")
        if p <= 3:
            continue
            
    #===============================
    #AÇÕES DAS PERGUNTAS 1

    #acerto:
    if r1 == resposta_level1:
        lista = acerto(dinheru, prox)
        dinheru = lista[0]
        prox = lista[1]
        
        
     #desistência:
    elif r1 == "parar":
        parar()
        break
        
    #erro:
    elif resposta_level1 == 'a':
        erroc()
        break
    elif resposta_level1 == 'b':
        errob()
        break
    elif resposta_level1 == 'c':
        erroc()
        break
    elif resposta_level1 == 'd':
        errod()
        break
           
#===============================
#PERGUNTAS LEVEL 2

pergunta1= [p6, p8, p12, p13, p14, p16, p17, p19, p62]
alternativa1= [a6, a8, a12, a13, a14, a16, a17, a19, a62]
resposta1=[r6, r8, r12, r13, r14, r16, r17, r19, r62]

while quant >= 5 and quant < 12:
    quant += 1
    x = quant
    if prox >= 5:
        if x == 6 and r1 != "4":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nAgora você está no nível 2! As perguntas valem $1.000.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        lista = pergunta()
        pergunta_level1 = lista[0];
        resposta_level1 = lista[1];
        alternativa_level1 = lista[2];
        
	#==============================
	#DIÁLOGO COM O USUÁRIO 2
            
        if x >= 6 and x <= 12:
            lista = dialogo2(x,errar2, parar2, acertar2)
            errar2= lista[0]
            parar2= lista[1]
            acertar2= lista[2]
        
        print("Para parar digite: parar")
        print ("\nAjudas: " + str(ajudas))
        print("")
    
        r1 = respostadousuario()
        print("")
        
	#==============================
	#AJUDAS 2
        
        #Convidados:
        if r1 == "1":
            r1 = convidados_level2()
                
        #Placas:
        elif r1 == "2":
            r1 = placas()
            
        #Cartas:
        elif r1 == "3":
            r1 = cartas()

        #Pular:
        elif r1 == "4":
            lista = pular(p,r1,quant)
            p = lista[0]
            r1 = lista[1]
            quant = lista[2]
            if p == 3:
                ajudas.remove("4. Pular")
            if p<= 3:
                continue
                    
	#===============================
	#AÇÕES DAS PERGUNTAS 2

        #acerto:
        if r1 == resposta_level1:
            lista = acerto(dinheru, prox)
            dinheru = lista[0]
            prox = lista[1]
            
         #desistência:
        elif r1 == "parar":
            parar()
            break
        #erro:
        elif resposta_level1 == 'a':
            erroa()
            break
        elif resposta_level1 == 'b':
            errob()
            break
        elif resposta_level1 == 'c':
            erroc()
            break
        elif resposta_level1 == 'd':
            errod()
            break

#===============================
#PERGUNTAS LEVEL 3

pergunta1= [p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34]
alternativa1= [a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34]
resposta1=[r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34]

while quant >= 12 and quant < 18:
    quant += 1
    x = quant
    if prox >= 12:
        if x == 12 and r1 != "4":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nAgora você está no nível 3! As perguntas valem $10.000.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        lista = pergunta()
        pergunta_level1 = lista[0];
        resposta_level1 = lista[1];
        alternativa_level1 = lista[2];
        
	#==============================
	#DIÁLOGO COM O USUÁRIO 3
         
        if x >= 12 and x <= 18:
            lista = dialogo2(x, errar2, parar2, acertar2)
            errar2= lista[0]
            parar2= lista[1]
            acertar2= lista[2]
        
        print("Para parar digite: parar")
        print ("\nAjudas: " + str(ajudas))
        print("")
    
        r1 = respostadousuario()
        print("")
        
	#==============================
	#AJUDAS 3
        
        #Convidados:
        if r1 == "1":
            r1 = convidados_level3()
                
        #Placas:
        elif r1 == "2":
            r1 = placas()
            
        #Cartas:
        elif r1 == "3":
            r1 = cartas()

        #Pular:
        elif r1 == "4":
            lista = pular(p,r1,quant)
            p = lista[0]
            r1 = lista[1]
            quant = lista[2]
            if p == 3:
                ajudas.remove("4. Pular")
            if p<= 3:
                continue
                    
	#===============================
	#AÇÕES DAS PERGUNTAS 3

        #acerto:
        if r1 == resposta_level1:
            lista = acerto(dinheru, prox)
            dinheru = lista[0]
            prox = lista[1]
            
         #desistência:
        elif r1 == "parar":
            parar()
            break
        #erro:
        elif resposta_level1 == 'a':
            erroa()
            break
        elif resposta_level1 == 'b':
            errob()
            break
        elif resposta_level1 == 'c':
            erroc()
            break
        elif resposta_level1 == 'd':
            errod()
            break

#===============================
#PERGUNTAS LEVEL 4

pergunta1= [p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54]
alternativa1= [a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52, a53, a54]
resposta1=[r35, r36, r37, r38, r39, r40, r41, r42, r43, r44, r45, r46, r47, r48, r49, r50, r51, r52, r53, r54]

while quant >= 18 and quant < 23:
    quant += 1
    x = quant
    if prox >= 18:
        if x == 18 and r1 != "4":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nAgora você está no nível 4! As perguntas valem $100.000.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        lista = pergunta()
        pergunta_level1 = lista[0];
        resposta_level1 = lista[1];
        alternativa_level1 = lista[2];
        
	#==============================
	#DIÁLOGO COM O USUÁRIO 4
         
        if x >= 18 and x <= 24:
            lista = dialogo2(x, errar2, parar2, acertar2)
            errar2= lista[0]
            parar2= lista[1]
            acertar2= lista[2]
        
        print("Para parar digite: parar")
        print ("\nAjudas: " + str(ajudas))
        print("")
    
        r1 = respostadousuario()
        print("")
        
	#==============================
	#AJUDAS 4
        
        #Convidados:
        if r1 == "1":
            r1 = convidados_level4()
                
        #Placas:
        elif r1 == "2":
            r1 = placas()
            
        #Cartas:
        elif r1 == "3":
            r1 = cartas()

        #Pular:
        elif r1 == "4":
            lista = pular(p,r1,quant)
            p = lista[0]
            r1 = lista[1]
            quant = lista[2]
            if p == 3:
                ajudas.remove("4. Pular")
            if p<= 3:
                continue
                    
	#===============================
	#AÇÕES DAS PERGUNTAS 4

        #acerto:
        if r1 == resposta_level1:
            lista = acerto(dinheru, prox)
            dinheru = lista[0]
            prox = lista[1]
            
         #desistência:
        elif r1 == "parar":
            parar()
            break
        #erro:
        elif resposta_level1 == 'a':
            erroa()
            break
        elif resposta_level1 == 'b':
            errob()
            break
        elif resposta_level1 == 'c':
            erroc()
            break
        elif resposta_level1 == 'd':
            errod()
            break

#===============================
#PERGUNTAS 1 MELAO

pergunta1= [p55, p56, p57, p58, p59, p60, p61]
alternativa1= [a55, a56, a57, a58, a59, a60, a61]
resposta1=[r55, r56, r57, r58, r59, r60, r61]

while quant == 23:
        quant +=1
        x = quant
        if prox >= 23:
            if x == 24 and r1 == "4":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\nAgora você está no último nível! Esta é a pergunta de 1 milhão! Você não pode mais usar as ajudas.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            lista = pergunta()
            pergunta_level1 = lista[0]
            resposta_level1 = lista[1]
            alternativa_level1 = lista[2]
        
	    #==============================
	    #DIÁLOGO COM O USUÁRIO 5
         
            if x == 24:
                lista = dialogo2(x, errar2, parar2, acertar2)
                errar2= lista[0]
                parar2= lista[1]
                acertar2= lista[2]
            
            print("Para parar digite: parar")
            print("")
        
            r1 = respostadasdicas()
            print("")
            
            #===============================
            #AÇÕES DAS PERGUNTAS 5
    
            #acerto:
            if r1 == resposta_level1:
                print("Você acertou! Ganhou 1 milhão! Parabéns! \nObs: sobre o pagamento, tire satisfações com os monitores.")
                
             #desistência:
            elif r1 == "parar":
                parar()
                break
            #erro:
            if r1 != resposta_level1:
                print("Você errou :/! Ganhou $300")
            
            quant +=1
