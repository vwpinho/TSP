import pygame
from pygame.locals import * 
import random
import math
import sys
import time

argv = sys.argv
t = time.time()
nvertices = int(argv[1])
width = 500
height = 500
count = 0
minDist = 99999
nGen = 0
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('TSP')
caminho = []
caminhoMin = []
grafo = []
populacao = []
score = []
popSize = int(argv[2])
mutRate = float(argv[3])
def calcDist(c):
    sum = 0
    for i in range (nvertices-1):
        index1 = c[i]
        index2 = c[i+1]
        d = dist(grafo[index1][0],grafo[index1][1],grafo[index2][0],grafo[index2][1])
        sum += d
    return sum

def dist( n1, n2, n3,  n4):
    n = math.sqrt(pow((n1-n3),2) + pow((n2-n4),2))
    return n

def calcScore():
    global populacao, minDist,caminhoMin,score
    score = []
    for i in range(len(populacao)):
        d = calcDist(populacao[i])
        if d < minDist:
            minDist = d
            caminhoMin = populacao[i].copy()
        score.append(1/(d+1))
def normalizeScore():
    s = 0
    global score
    for i in range(len(score)):
        s += score[i]
    for i in range(len(score)):
        score[i] = score[i] / s

def pickOne():
    global score, populacao
    index = 0
    r = random.random()
    while(r > 0):
        r -= score[index]
        index += 1
    index -= 1
    return populacao[index].copy()

def crossOver(seq1,seq2):
    ini = random.randint(0, len(seq1)-1)
    end = random.randint(ini, len(seq1)-1)
    newSeq = seq1[ini:end]
    for i in range(len(seq2)):
        c = seq2[i]
        if newSeq.count(c)==0:
            newSeq.append(c)
    return newSeq
    

def mutate(seq):
    id1 = random.randint(0,len(seq)-1)
    id2 = random.randint(0,len(seq)-1)
    aux = seq[id1]
    seq[id1] = seq[id2]
    seq[id2] = aux
    return seq

# Melhorar
# Usando a funcao prob pickOne temos selecao
def nextGen():
    global populacao
    newPop = []
    for i in range(len(populacao)):
        ind1 = pickOne()
        ind2 = pickOne()
        ind = crossOver(ind1,ind2)
        if(random.random() < mutRate):
            ind = mutate(ind)
        newPop.append(ind)
    populacao = newPop



for i in range(nvertices):
    grafo.append((random.randint(0,width),random.randint(0,height)))
    caminho.append(i)
for i in range(popSize):
    populacao.append(caminho.copy())
    random.shuffle(populacao[i])
# calcula score
# calcScore()
# # Normaliza score
# normalizeScore()

pygame.init()


while True:
    screen.fill((0,0,0))
    aux = []
    calcScore()
    normalizeScore()
    nextGen()
    nGen += 1
    print("Elapsed time:", (time.time() -t), "sec" )
    for i in range(len(grafo)):
        pygame.draw.circle(screen,(255,255,255),grafo[i],10)
    for i in range(nvertices):
        aux.append(grafo[caminhoMin[i]])
    pygame.draw.lines(screen,(0,100,0),False,aux,5)   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
    pygame.time.wait(100)