print (" Pobre ou Rico ? O que voce sera ? ")
pontos=0
fase1 = '''\
1- Como voce se descreve? 
a)legal/feliz
b)preguicoso/pessimista
c)pratico/realista
d)confiante/otimista
'''
print(fase1)
resposta1 = input ()
if resposta1=="a":
    pontos+=10
if resposta1=="b":
    pontos+=0
if resposta1=="c":
    pontos+=30
if resposta1=="d":
    pontos+=20
print(pontos)

fase2 = '''\
2- Qual nivel de educação que voce gostaria de ter?
a) primario
b) fundamental
c) ensino medio
d) mestrado/doutorado
'''
print(fase2)
resposta2 = input ()
if resposta2=="a":
    pontos+=0
if resposta2=="b":
    pontos+=10
if resposta2=="c":
    pontos+=20
if resposta2=="d":
    pontos+=30
print(pontos)

fase3 = '''\
3- O que é mais importante para voce ?
a) familia
b) poder/sucesso
c) conhecimento/habilidade
d) nada
'''
print(fase3)
resposta3 = input ()
if resposta3=="a":
    pontos+=20
if resposta3=="b":
    pontos+=30
if resposta3=="c":
    pontos+=10
if resposta3=="d":
    pontos+=0
print(pontos)

fase4= '''\
4-Sua família é rica ?
a)Eu sou de uma família de classe média
b)Sim!
c)Eu não tenho família
d)Não
'''
print(fase4)
resposta4= input ()
if resposta4=="a":
    pontos+=20
if resposta4=="b":
    pontos+=30
if resposta4=="c":
    pontos+=0
if resposta4=="d":
    pontos+=10
print(pontos)

fase5= '''\
5- Qual a cabeça que voce colocaria na nota de cem dolares ?
a) homem de ferro
b) palhaço
c) homem aranha
d) minha cara
'''
print(fase5)
resposta5= input ()
if resposta5=="a":
    pontos+=20
if resposta5=="b":
    pontos+=0
if resposta5=="c":
    pontos+=10
if resposta5=="d":
    pontos+=30
print(pontos)

fase6= '''\
6- Se voce ficasse milionario o que iria fazer ?
a) gastar com festas
b) ajudar a familia
c) investir em negócios
d) ajudar quem precisa
'''
print(fase6)
resposta6= input ()
if resposta6=="a":
    pontos+=0
if resposta6=="b":
    pontos+=20
if resposta6=="c":
    pontos+=30
if resposta6=="d":
    pontos+=10
print(pontos)

fase7='''\
7-voce ficaria horas em um banheiro cheio de insetos por dinheiro ? Tipo 2 milhões?
a)De jeito nenhum
b)talvez,ficaria até por menos
c)sim,até por mais dinheiro
d)Nunca, é bem nojento
'''
print(fase7)
resposta7= input ()
if resposta7=="a":
    pontos+=0
if resposta7=="b":
    pontos+=30
if resposta7=="c":
    pontos+=20
if resposta7=="d":
    pontos+=10
print(pontos)

fase8='''\
8-Se voce tivesse que escolher seu parceiro(a) qual voce escolheria ?
a)pobre e bonita
b)classe média e inteligente
c)rico e ganancioso(a)
d)por amor
'''
print(fase8)
resposta8= input()
if resposta8=="a":
    pontos+=10
if resposta8=="b":
    pontos+=20
if resposta8=="c":
    pontos+=30
if resposta8=="d":
    pontos+=0
print(pontos)

fase9= '''\
9- Com as opcoes abaixo, qual delas voce queria ser?
a) pobre e bonito
b) rico e humilde
c) normal e inteligente
d) do jeito que voce e mesmo
'''
print(fase9)
resposta9= input()
if resposta9=="a":
    pontos+=0
if resposta9=="b":
    pontos+=30
if resposta9=="c":
    pontos+=10
if resposta9=="d":
    pontos+=20
print(pontos)

fase10= '''\
10- Como voce se ver daqui uns anos?
a) bem de vida
b) feliz
c) pobre
d) ou nao se ve ainda
'''
print(fase10)
resposta10= input ()
if resposta10=="a":
    pontos+=30
if resposta10=="b":
    pontos+=20
if resposta10=="c":
    pontos+=0
if resposta10=="d":
    pontos+=10
print(pontos)

if pontos>=210:
   print("voce vai ser rico!!!")

else: 
   print("voce vai ser pobre!!!")
