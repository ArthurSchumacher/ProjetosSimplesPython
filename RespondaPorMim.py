import random

def op():
    op = int(input('[0] Sair | [1] Fazer uma pergunta: '))
    return op

programAnswers = ('Sim', 'Nao', 'Talvez')

while (op() != 0):
    listReader = random.randint(0, 2)

    playerQuestion = str(input('\nDigite sua pergunta: '))
    print('Programa:', programAnswers[listReader], '\n')