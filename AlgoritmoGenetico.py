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


def avaliar(populacao, tamPopulacao, precind):
    fitness = []
    somatotal = 0

    for j in range(tamPopulacao):

        cromossomo = ''.join(populacao[j])
        dec = int(cromossomo, 2)

        maximo = 5.12
        minimo = -5.12

        x = minimo+(maximo-minimo)*dec/(2**precind)
        print('X: {}'.format(x))

        somatotal = somatotal + (2**x)
        print('F(x): {}'.format(somatotal))

        fitness.append(somatotal)

    return fitness


def selecao(fitness, populacao):
    populacaoIntermediaria=[]
    somatotal = sum(fitness)

    for i in range(tamPopulacao):
        r = uniform(0, somatotal)
        if (fitness[i] > r):
            populacaoIntermediaria.append(populacao[i])

    print('População Intermediaria: {}'.format(populacaoIntermediaria))

    return  populacaoIntermediaria


def roda_roleta(fitness, populacao):

    total = sum(fitness)
    r = uniform(0, total)
    sorteado = 0
    for i in range(len(fitness)):

        if (fitness[i] > r):

            sorteado = populacao[i]

    print('Sorteado: {}'.format(sorteado))
    return  sorteado


if __name__ == '__main__':
    precind = 6
    precvar = 2
#   nfob = 2
    tamPopulacao = int(input('Quantidade "Par" da população: '))
#   probMutacao = float(input('Probabilidade de mutação: '))
#   probCrossover = float(input('Probabilidade de crossover: '))

    populacao = inicia_populacao(tamPopulacao, precind)
    fitness = avaliar(populacao, tamPopulacao, precind)

#    for j in range(nfob):
    sel = selecao(fitness, populacao)
    roda_roleta(fitness,sel)

