import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
from model.board import Board

def fitness(chromosome):
    score = 0
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if j + chromosome[j] == i + chromosome[i]:
                continue
            elif j - chromosome[j] == i - chromosome[i]:
                continue
            elif i == j :
                continue
            score += 1
    return score / 2

def cross_over(par1, par2, n):
    


p = 10
n = 4
community = []
fitnesses = []


for _ in range(p):
    community.append(Board(n))

for i in community:
    fitnesses.append(fitness(i.grid))

community_fitness = dict(zip(community,fitnesses))
community_fitness = dict(sorted(community_fitness.items(), key=lambda item: item[1], reverse=True))

