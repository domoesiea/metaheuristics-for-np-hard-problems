import random
import numpy as np

def glouton(c,v,score):

    

    resultatGLPK = 73
    
    Solutions=[]

    score=np.array(score)
    while(np.sum(score==-1)<len(score)):
        index=np.argmax(score)
        Solutions.append(index)
        score[index]=-1
        for i in range(len(score)):
            if(score[i]!=-1 and i not in v[index]):
                score[i]=-1
    
    #print("Les index des variables solutions sont",Solutions)   
    Scorefinal=0
    for i in range(len(Solutions)):
        Scorefinal=Scorefinal+c[Solutions[i]]
    #print("Le score final est de",Scorefinal)
    return (Solutions, Scorefinal)
   # print("Le Gap est de ",(round((resultatGLPK-Scorefinal)/resultatGLPK,2)))


def gloutonRandomise(c,v,score):

 
 
    Solutions=[]


    score=np.array(score)
    for i in range(len(score)):
        resultat = random.choice([0, 1])
        if(resultat==1):
            score[i]=-1

    while(np.sum(score==-1)<len(score)):
        index=np.argmax(score)
        Solutions.append(index)
        score[index]=-1
        for i in range(len(score)):
            if(score[i]!=-1 and i not in v[index]):
                score[i]=-1
    
    #print("Les index des variables solutions sont",Solutions)   
    Scorefinal=0
    for i in range(len(Solutions)):
        Scorefinal=Scorefinal+c[Solutions[i]]
    #print("Le score final est de",Scorefinal)
    return (Solutions,Scorefinal)
   # print("Le Gap est de ",(round((resultatGLPK-Scorefinal)/resultatGLPK,2)))

def gloutonreparation(c,v,tab,score):
    
    Solutions=[]
    score=np.array(score)

    ''' for i in range(len(score)):
        resultat = random.choice([0, 1])
        if(resultat==1):
            score[i]=-1'''
    
    if (len(tab))>0:
        for i in range(len(tab)):
            index=tab[i]
            Solutions.append(index)
            score[index]=-1
            for j in range(len(score)):
                if(score[j]!=-1 and j not in v[index]):
                    score[j]=-1

    while(np.sum(score==-1)<len(score)):
        index=np.argmax(score)
        Solutions.append(index)
        score[index]=-1
        for i in range(len(score)):
            if(score[i]!=-1 and i not in v[index]):
                score[i]=-1

    return Solutions


def gloutonTabou(c,v,tab,valinterdite,valinterdite2,score):
    
    Solutions=[]
    score=np.array(score)

    
    score[valinterdite]=-1
    score[valinterdite2]=-1


    if (len(tab))>0:
        for i in range(len(tab)):
            index=tab[i]
            Solutions.append(index)
            score[index]=-1
            for j in range(len(score)):
                if(score[j]!=-1 and j not in v[index]):
                    score[j]=-1


    while(np.sum(score==-1)<len(score)):
        index=np.argmax(score)
        Solutions.append(index)
        score[index]=-1
        for i in range(len(score)):
            if(score[i]!=-1 and i not in v[index]):
                score[i]=-1
    
    
    return Solutions