from random import *

__author__ = 'Patrick Amaral'

def inicia_populacao(tamPopulacao, precind):
    populacao = []
    print('\nPOPULAÇÃO INICIAL')
    print('-----' * 6)
    for j in range(tamPopulacao):
        linha = []

        for i in range(precind):
            linha.append(str(randint(0,1)))

        populacao.append(linha)
        print('{}'.format(linha))
    return populacao


def avaliar(populacao,  tamPopulacao, precind, precvar):
    print('\nAVALIAÇÃO DA POPULAÇÃO')
    print('-----' * 6)
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
        print('Fitness: {}'.format(fitness[j]))

    return fitness


def selecao(fitness):

    somatotal = sum(fitness)
    probSelecao = []
    pacum = []

    for j in range(0, len(fitness)):
        probSelecao.append(fitness[j]/somatotal)
        pacum.append(sum(probSelecao))
    print('\nPOPULAÇÃO SELECIONADA')
    print('-----'*6)
    for j in range(tamPopulacao):

        i = 0
        parcial = 0
        r = uniform(0, somatotal)

        while (i != len(pacum)):

            parcial += pacum[i]
            i += 1
            if (parcial >= r):
                break
        populacao.__setitem__(j, populacao[i-1])
        print('{}'.format(populacao[i-1]))



def crossover(probCrossover):
    indices = []
    randoms = []

    print('\nCROSSOVER')
    print('-----'*6)
    for i in range(len(populacao)):
        randoms.append(random())

    for i , r in enumerate(randoms):
        if r <= probCrossover:
            indices.append(i)

    if len(indices)%2!=0:
        indices.pop()
    print('\nINDICES: {}'.format(indices))
    for ind in range(0, len(indices), 2):

        pontoCorte = randint(1, precind)
        print('Corte em: {}'.format(pontoCorte))
        print('Pai: {}\nMae: {}'.format(populacao[indices[ind]], populacao[indices[ind+1]]))
        filho1 = populacao[indices[ind]][0:pontoCorte]+populacao[indices[ind+1]][pontoCorte:]
        filho2 = populacao[indices[ind+1]][0:pontoCorte]+populacao[indices[ind]][pontoCorte:]

        populacao.__setitem__(indices[ind], filho1)
        populacao.__setitem__(indices[ind+1], filho2)


def mutacao(probMutacao):
    for j in range(len(populacao)):
        for i in range(len(populacao[j])):

            ra = random()
            if ra <= probMutacao:

                if (populacao[j][i] == '1'):
                     populacao[j].__setitem__(i, '0')
                elif (populacao[j][i] == '0'):
                     populacao[j].__setitem__(i, '1')

if __name__ == '__main__':
    precind = 6
    precvar = 2
    nfob = 10

    tamPopulacao = int(input('Quantidade "Par" da população: '))
    probMutacao = float(input('Probabilidade de mutação: '))
    probCrossover = float(input('Probabilidade de crossover: '))

    populacao = inicia_populacao(tamPopulacao, precind)
    fitness = avaliar(populacao, tamPopulacao, precind, precvar)

    for j in range(nfob):
        selecao(fitness)
        crossover(probCrossover)
        print('\nPOPULAÇÃO CROSSOVER')
        print('-----' * 6)
        for i in range(len(populacao)):
            print('{}'.format(populacao[i]))
        mutacao(probMutacao)
        print('\nPOPULAÇÃO MUTAÇÃO')
        print('-----' * 6)
        for i in range(len(populacao)):
            print('{}'.format(populacao[i]))
        fitness = avaliar(populacao, tamPopulacao, precind, precvar)
