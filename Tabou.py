from glouton import gloutonTabou
from random import random,randint


'''def RechercheVoisinage2(c,v,Solution,score,tabou,prof): #enlève 2 individus
    if(prof>=3):
        return []
    tabou.append(Solution)
    resultats=[]
    for i in range(len(Solution)):
            tmpSolution=Solution[:]
            valinterdite=tmpSolution[i]
            tmpSolution.pop(i)
            for j in range(len(tmpSolution)):
                tmpSolution2=tmpSolution[:]
                valinterdite2=tmpSolution2[j]
                tmpSolution2.pop(j)
                tmpSolution2=gloutonTabou(c,v,tmpSolution2,valinterdite,valinterdite2)
                
                tmpscore=0
                for k in range(len(tmpSolution2)):
                    tmpscore=tmpscore+c[tmpSolution2[k]]
                if(tmpscore>=score and tmpSolution2 not in tabou):
                    resultats.append([tmpSolution2,tmpscore])
                    tab=RechercheVoisinage2(c,v,tmpSolution2,tmpscore,tabou,prof+1)
                    if(len(tab)>0):
                        resultats.append(tab)
    if(len(resultats)>0):
        resultats=max(resultats, key= lambda x: x[1])
    return resultats'''
    
    

def RechercheVoisinageComplet(c,v,Solution,score,tabou,prof,scoretab): #enlève 1 individu
    if(prof>=3):
        return []
    tabou.append(Solution)
    resultats=[]
    for i in range(len(Solution)):
            tmpSolution=Solution[:]
            valinterdite=tmpSolution[i]
            tmpSolution.pop(i)
            tmpSolution=gloutonTabou(c,v,tmpSolution,valinterdite,valinterdite,scoretab)
            
            tmpscore=0
            for k in range(len(tmpSolution)):
                tmpscore=tmpscore+c[tmpSolution[k]]
            if(tmpscore>=score and tmpSolution not in tabou):
                resultats.append([tmpSolution,tmpscore])
                tab=RechercheVoisinageComplet(c,v,tmpSolution,tmpscore,tabou,prof+1,scoretab)
                if(len(tab)>0):
                    resultats.append(tab)
    if(len(resultats)>0):
        resultats=max(resultats, key= lambda x: x[1])
    return resultats

def RechercheVoisinageSimple(c,v,Solution,score,tabou,scoretab): #enlève 1 individu
    tabou.append(Solution)
    for i in range(round(len(Solution)/2)): 
        tmpSolution=Solution[:]
        index=randint(0,len(tmpSolution)-1)
        valinterdite=tmpSolution[index]
        tmpSolution.pop(index)
        tmpSolution=gloutonTabou(c,v,tmpSolution,valinterdite,valinterdite,scoretab)
        tmpscore=0
        for k in range(len(tmpSolution)):
            tmpscore=tmpscore+c[tmpSolution[k]]
        if(tmpscore>score and tmpSolution not in tabou):
            Solution=tmpSolution
            score=tmpscore
            tabou.append(Solution)
    return [Solution,score]
    


def Tabou(c,v,Solution,score,small):

    Score=Solution[1]
    Solution=Solution[0]
    
    
    if(small==True):
        resultats=RechercheVoisinageComplet(c,v,Solution,Score,[],0,score)
    else:
        resultats=RechercheVoisinageSimple(c,v,Solution,Score,[],score)
    
    

    if(len(resultats)==0):
        
        return Solution
        
    else:
        
        return resultats[0]
    
    
    