import pygame
from pygame.locals import * 
import random
import math
import time
import sys

arg = sys.argv
t = time.time()
nvertices = int(arg[1])
width = 500
height = 500
count = 0
minDist = 99999
caminhoMin = []
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('TSP')

caminho = []
grafo = []
for i in range(nvertices):
    grafo.append((random.randint(0,width),random.randint(0,height)))
    caminho.append(i)

pygame.init()

def permute():
    maiorI = -1
    for i in range(len(caminho)-1):
        if caminho[i] < caminho[i+1]:
            maiorI = i
    if maiorI == -1:
        return -1
    maiorJ = -1
    for j in range(len(caminho)):
        if caminho[maiorI] < caminho[j]:
            maiorJ = j

    swap = caminho[maiorI]
    caminho[maiorI] = caminho[maiorJ]
    caminho[maiorJ] = swap
    
    n = len(caminho)
    aux = []
    for i in range (maiorI+1,n):
        aux.append(caminho.pop())
    k = 0
    for i in range (maiorI+1,n):
        caminho.append(aux[k])
        k += 1
    #print(caminho)
  
def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)

def calcDist():
    sum = 0
    for i in range (nvertices-1):
        index1 = caminho[i]
        index2 = caminho[i+1]
        d = dist(grafo[index1][0],grafo[index1][1],grafo[index2][0],grafo[index2][1])
        sum += d
    return sum

def dist( n1, n2, n3,  n4):
    n = math.sqrt(pow((n1-n3),2) + pow((n2-n4),2))
    return n



#print(caminho)
fnv = fat(nvertices)
while True:
    screen.fill((0,0,0))
    aux = []
    for i in range(len(grafo)):
        pygame.draw.circle(screen,(255,255,255),grafo[i],10)
    for i in range(nvertices):
        aux.append(grafo[caminho[i]])
    pygame.draw.lines(screen,(0,100,0),False,aux,5)   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    count += 1
    d = calcDist()
    if (d < minDist):
        minDist = d
        print(minDist)
        caminhoMin = caminho.copy()
    #print(d)
    #print('{}% completo'.format(count*100/fnv))
    if(permute() == -1):
        print("Elapsed time:", (time.time() -t), "sec")
        screen.fill((0,0,0))
        aux = []
        for i in range(len(grafo)):
            pygame.draw.circle(screen,(255,255,255),grafo[i],10)
        for i in range(nvertices):
            aux.append(grafo[caminhoMin[i]])
        pygame.draw.lines(screen,(100,0,0),False,aux,5)
        print(minDist)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
    pygame.display.update()
    pygame.time.wait(100)