introduçao = "introducao.txt"
arquivo = open(introduçao, "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

x=1
respostas_usuario=[]
perguntas = {1:"\n1. Normalmente, quantos litros de sangue uma pessoa tem?",
             2:"\n2.De quem é a famosa frase 'Penso, logo existo'?",
             3:"\n3. De onde é a invenção do chuveiro elétrico?",
             4:"\n4. Quais o menor e o maior país do mundo?",
             5:"\n5.Qual o livro mais vendido no mundo a seguir á Bíblia?",
             6:"\n6.Quantas casas decimais tem o número pi?",
             7:"\n7.Atualmente, quantos elementos químicos a tabela periódica possui?",
             8:"\n8.Qual o número mínino de jogadores numa partida de futebol?",
             9:"\n9.Quanto tempo a luz do Sol demora a chegar á Terra?",
             10:"\n10.Em que período da pré-história o fogo foi descoberto?"}

respostas = {1:"\nA) Tem entre 2 a 4 litros. \nB) Tem entre 4 a 6 litros. \nC) Tem 10 litros \nD) Tem 7 litros",
             2:"\nA)Platão. \nB)Galileu Galilei. \nC)Descartes \nD)Sócrates",
             3:"\nA)França. \nB)Inglaterra. \nC)Brasil. \nD)Austrália",
             4:"\nA)Vaticano e Rússia. \nB)Nauru e China. \nC)Malta e Estados Unidos. \nD)São Marino e Índia",
             5:"\nA)O Senhor dos Anéis. \nB)Dom Quixote. \nC)O Pequeno Príncipe. \nD)Ela, a Feiticeira",
             6:"\nA)Duas. \nB)Centenas. \nC)Trilhares. \nD)Vinte",
             7:"\nA)113. \nB)109. \nC)108. \nD)118",
             8:"\nA)8. \nB)10. \nC)7. \nD)5",
             9:"\nA)12 minutos. \nB)8 minutos. \nC)1 dia. \nD)Segundos",
             10:"\nA)Neolítico. \nB)Paleolítico. \nC)Idade dos Metais. \nD)Período da Pedra Polida"}
             
gabarito= ["B","C","C","A","B","C","D","C","B","B"]

while x<=len(perguntas):
    print(perguntas[x])
    print(respostas[x])
    resposta = input("Resposta: ").upper()
    respostas_usuario.append(resposta)
    x+=1
print("\nSuas respostas: ",respostas_usuario)
print("Gabarito: ",gabarito)

contador=0
respostas_certas = 0
for contador in range(0,len(gabarito)):
    if respostas_usuario[contador]== gabarito[contador]:
        respostas_certas+=1


porcentagem =  (100*respostas_certas)/10    
print("\nVocê acertou {} ({}%)!".format(respostas_certas, porcentagem))
