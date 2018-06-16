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


def avaliar(populacao,  tamPopulacao, precind, precvar):
    fitness = []
    somatotal = 0

    for j in range(tamPopulacao):

        for i in range(0, precind, precvar):
            individuo = ''.join(populacao[j][i:i + precvar])

            dec = int(individuo, 2)

            maximo = 5.12
            minimo = -5.12

            x = minimo+(maximo-minimo)*dec/(2**precind)

            somatotal = somatotal + (2**x)
            print('F(x): {}'.format(somatotal))

        fitness.append(somatotal)
    print('Fitness: {}'.format(fitness))

    return fitness


def selecao(fitness, populacao):
    populacaoIntermediaria=[]
    somatotal = sum(fitness)
    probSelecao = []
    pacum = []

    for j in range(0, len(fitness)):
        probSelecao.append(fitness[j]/somatotal)
        pacum.append(sum(probSelecao))

    for j in range(tamPopulacao):

        i = 0
        parcial = 0
        r = uniform(0, somatotal)

        while (i != len(pacum)):

            parcial += pacum[i]
            i += 1
            if (parcial >= r):
                break
        populacaoIntermediaria.append(populacao[i-1])

    print('População Intermediaria: {}'.format(populacaoIntermediaria))

    return  populacaoIntermediaria

def crossover(populacao, probCrossover):
    indices = []
    randoms = []

    for i in range(len(populacao)):
        randoms.append(random())
    print('randoms {}'.format(randoms))

    for i , r in enumerate(randoms):
        if r <= probCrossover:
            indices.append(i)

    if len(indices)%2!=0:
        indices.pop()
    print('Indices {}'.format(indices))


    for ind in range(0, len(indices), 2):
        i = indices[ind]
        pontoCorte = randint(1, precind)
        print('Corte em: {}'.format(pontoCorte))
        print('Pai: {}\nMae: {}'.format(populacao[i], populacao[i+1]))

        filho1 = populacao[i][0:pontoCorte]+populacao[i+1][pontoCorte:]
        filho2 = populacao[i+1][0:pontoCorte]+populacao[i][pontoCorte:]
        print('Filho 1: {}\nFilho 2: {}'.format(filho1, filho2))

    return filho1, filho2

def mutacao(individuo1, individuo2):
    r = randint(0,precvar)
    ra = random()

    if ra <= probMutacao:
        if (individuo1[r] == 1):
            individuo1[r]=0
        elif (individuo1[r] == 0):
            individuo1[r] = 1

        if (individuo2[r] == 1):
            individuo2[r]=0
        elif (individuo2[r] == 0):
            individuo2[r] = 1

    return individuo1, individuo2

if __name__ == '__main__':
    precind = 6
    precvar = 2
    nfob = 2
    tamPopulacao = int(input('Quantidade "Par" da população: '))
    probMutacao = float(input('Probabilidade de mutação: '))
    probCrossover = float(input('Probabilidade de crossover: '))

    populacao = inicia_populacao(tamPopulacao, precind)
    fitness = avaliar(populacao, tamPopulacao, precind, precvar)

#    for j in range(nfob):
    sel = selecao(fitness, populacao)
    crossover(sel, probCrossover)

