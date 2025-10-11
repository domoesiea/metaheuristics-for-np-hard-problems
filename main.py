import sys
from genetic import Genetic
from time import time
from glouton import glouton,gloutonRandomise
from Tabou import Tabou

if len(sys.argv) < 4:
    print("Il manque des arguments")
else:
    start=time()
    file = open(sys.argv[2], "r")
    lines = file.readlines()
    file.close()
    n, m = int(lines[0].split()[0]), int(lines[0].split()[1]) # n=contraintes et m nombre d'individus
    c=[]
    v=[]
    score=[]
    for i in range(1,n+1):
        c.append(int(lines[i].split()[1]))
        v.append([])

    for i in range(n+1,len(lines)):
        v[int(lines[i].split()[0])].append(int(lines[i].split()[1]))
        if(int(lines[i].split()[0]) not in v[int(lines[i].split()[1])]):
            v[int(lines[i].split()[1])].append(int(lines[i].split()[0]))

    for i in range(len(c)):
        score.append(c[i]*len(v[i]))
    
    
    Solution=Genetic(c,v,score,n,m,start,float(sys.argv[1]))
    
    with open(sys.argv[3], 'w') as file:
        for i in range(m):
            if(i not in Solution):
                file.write("0")
            else:
                file.write("1")
            file.write(" ")
    
    end=time()
    duree=end-start        
    #print(round(duree,2),"secondes")