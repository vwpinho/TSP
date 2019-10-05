import pygame
from pygame.locals import * 
import random
import math

nvertices = 5
width = 500
height = 500
count = 0
minDist = 99999
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('TSP')
caminho = []
caminhoMin = []
grafo = []
populacao = []
score = []

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

def nextGen():
    global populacao
    newPop = []
    for i in range(len(populacao)):
        ind = pickOne()
        newPop.append(ind)
    populacao = newPop



for i in range(nvertices):
    grafo.append((random.randint(0,width),random.randint(0,height)))
    caminho.append(i)
for i in range(10):
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