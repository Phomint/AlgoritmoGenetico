from random import *

__author__ = 'Patrick Amaral'

def inicia_populacao(tamPopulacao, precind):
    populacao = []

    for j in range(tamPopulacao):
        linha = []

        for i in range(precind):
            linha.append(str(randint(0,1)))

        populacao.append(linha)
        print('População [{}] = {}'.format(j, linha))
    return populacao


def avaliar(populacao, tamPopulacao, precind, precvar):
    fitness = []
    linha = []
    for j in range(tamPopulacao):

        somatotal = 0
        for i in range(0, precind, precvar):

            cromossomo =''.join(populacao[j][i:i+precvar])
            print('Cromossomo: {}'.format(cromossomo))
            dec = int(cromossomo, 2)

            maximo = 5.12
            minimo = -5.12

            x = minimo+(maximo-minimo)*dec/(2**precvar)
            print('X{}: {}'.format(i,x))

            somatotal = somatotal + (2**x)
            print('F(x{}): {}'.format(i,somatotal))

            linha.append(somatotal)

        fitness.append(sum(linha))

    return fitness


if __name__ == '__main__':
    precind = 256
    precvar = 16
    nfob = 2
    tamPopulacao = int(input('Quantidade "Par" da população: '))
#    probMutacao = float(input('Probabilidade de mutação: '))
#   probCrossover = float(input('Probabilidade de crossover: '))

    populacao = inicia_populacao(tamPopulacao, precind)
    fitness = avaliar(populacao, tamPopulacao, precind, precvar)

