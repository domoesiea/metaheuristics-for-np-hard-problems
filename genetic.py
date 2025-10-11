import numpy as np
from random import random,randint,choices
from glouton import glouton,gloutonRandomise,gloutonreparation
from Tabou import Tabou
from time import time


def Testemps(debut,temps,Bestscore,Bestsolution):
    fin=time()
    if(fin-debut>temps):
        #print(Bestscore)
        #print(Bestsolution)
        return 1
    else:
        return 0

    

def Genetic(c,v,score,n,m,debut,temps):

    TaillePopulation=400
    Probacroisement=0.8
    
    TailleSelection=100        
    Mutation=2  

    if(m<70000):
        Tabouactive=False
        ProbaTabou=1

    else:
        TaillePopulation=120
        TailleSelection=60  

        Tabouactive=False
        ProbaTabou=0.5
       

    
    
    
    
    Population=[]
    ScorePopulation=[]
    
    Solution=glouton(c,v,score)
    Population.append(Solution[0])
    Bestsolution=Solution[0][:]
    Bestscore=int(Solution[1])
    ScorePopulation.append(Solution[1])
    
    for i in range(TaillePopulation-1):
        Solution=gloutonRandomise(c,v,score)
        Population.append(Solution[0])
        ScorePopulation.append(Solution[1])
   
    
    while(1): #Sélection Parents
        if(Testemps(debut,temps,Bestscore,Bestsolution)==1):
            return Bestsolution
        start2=time()
        ScorePopulation=np.array(ScorePopulation)
        Fitness=[]
        Parents=[]
        tabindex=[]
        for i in range(len(Population)):
            tabindex.append(i)    

        for i in range(len(Population)):
            Fitness.append(ScorePopulation[i]/np.sum(ScorePopulation))
        for i in range(TailleSelection):
            Parents.append(choices(tabindex,Fitness,k=1)[0])
            tabindex.pop(Parents[i])
            Fitness.pop(Parents[i])
            for j in range(len(tabindex)):
                if(tabindex[j]>Parents[i]):
                    tabindex[j]=tabindex[j]-1
        

        
        for i in range(len(Parents)):
            Parents[i]=Population[Parents[i]]

      

        K=[] #Croisement à 2 points
        for i in range(len(Parents)):
            if(i%2==0):
                min2=len(Parents[i])
            else:
                if(len(Parents[i])<min2):
                    min2=len(Parents[i])
                K.append(randint(1,min2))
                K.append(None)

        Enfants=[]
        
        for i in range(len(Parents)):
            if(i%2==1):
                continue
            if(random()<Probacroisement):
                Enfant1=[]
                Enfant2=[]
                for j in range(K[i]):
                    Enfant1.append(Parents[i][j])
                    Enfant2.append(Parents[i+1][j])
                for j in range(len(Parents[i])-K[i]):
                    Enfant2.append(Parents[i][K[i]+j])
                for j in range(len(Parents[i+1])-K[i]):    
                    Enfant1.append(Parents[i+1][K[i]+j])
                Enfants.append(Enfant1)
                Enfants.append(Enfant2)
            else:
                Enfants.append(Parents[i])
                Enfants.append(Parents[i+1])

        for i in range(len(Enfants)): #mutation
            for j in range(len(Enfants[i])):
                if(random()<Mutation/(len(Enfants[i]))):
                    Enfants[i][j]=randint(0,n-1)


        ProblemScore=[]
        
        for i in range(len(Enfants)): # Reparation
            ProblemScore.append([])
            for j in range(len(Enfants[i])):
                ProblemScore[i].append(0)
                for k in range(len(Enfants[i])):
                    if(j!=k and Enfants[i][k] not in  v[Enfants[i][j]]):
                        ProblemScore[i][j]=ProblemScore[i][j]+1




        while(np.sum(np.sum(tableau) for tableau in ProblemScore)!=0):
            
            if(Testemps(debut,temps,Bestscore,Bestsolution)==1):
                return Bestsolution
            FitnessProblem = [(np.array(ProblemScore[i]) / len(Enfants[i])) for i in range(len(Enfants))]
            
            tabindex = [[j for j in range(len(Enfants[i]))] for i in range(len(Enfants))]

            for i in range(len(Enfants)):
                if(sum(ProblemScore[i])==0):
                    continue
                FitnessProblem.extend(np.array(ProblemScore[i]) / np.sum(ProblemScore[i]))
                

            for i in range(len(Enfants)):
                if(np.sum(ProblemScore[i])==0 or len(Enfants[i])==0):
                    continue
                FitnessProblem[i]=np.array(FitnessProblem[i]/np.sum(FitnessProblem[i])) #print normalisation probas
                indexsupp=np.random.choice(tabindex[i],p=FitnessProblem[i])
                
                
                tabindex[i]=np.delete(tabindex[i],indexsupp)              
                FitnessProblem[i]=np.delete(FitnessProblem[i],indexsupp)
                ProblemScore[i]=np.delete(ProblemScore[i],indexsupp)                
                if(indexsupp>=len(Enfants[i])):
                    indexsupp=len(Enfants[i])-1
                Enfants[i].pop(indexsupp)
                tabindex[i] = [idx - 1 if idx > indexsupp else idx for idx in tabindex[i]]
            
            ProblemScore=[]

            for i in range(len(Enfants)): 
                ProblemScore.append([])
                for j in range(len(Enfants[i])):
                    ProblemScore[i].append(0)
                    for k in range(len(Enfants[i])):
                        if(j!=k and Enfants[i][k] not in  v[Enfants[i][j]]):
                            ProblemScore[i][j]=ProblemScore[i][j]+1




            
        for i in range(len(Enfants)):
            if(Testemps(debut,temps,Bestscore,Bestsolution)==1):
                return Bestsolution
            Enfants[i]=gloutonreparation(c,v,Enfants[i],score)
            if(Tabouactive==True):
                if(random()<ProbaTabou and n<301 and m <20000):
                    scoreenfant=0
                    
                    for j in range(len(Enfants[i])):
                        scoreenfant=scoreenfant+c[Enfants[i][j]]
                    
                    Enfants[i]=Tabou(c,v,[Enfants[i],scoreenfant],score,True)
                else:
                    scoreenfant=0
                    
                    for j in range(len(Enfants[i])):
                        scoreenfant=scoreenfant+c[Enfants[i][j]]
                    
                    Enfants[i]=Tabou(c,v,[Enfants[i],scoreenfant],score,False)
            

                
                              
        Population.extend(Enfants)    
        scorefinal=[]
        for i in range(len(Population)):
            scorefinal.append(0)
            for j in range(len(Population[i])):
                scorefinal[i]=scorefinal[i]+c[Population[i][j]]

        
        scorefinal=np.array(scorefinal)
        indices=np.argsort(scorefinal)
        indices=indices[::-1]
        
        PopulationTmp=[]
        for i in range(TaillePopulation):
            PopulationTmp.append(Population[indices[i]])
        Population=PopulationTmp

        
        if(Bestscore<max(scorefinal)):
            Bestsolution=Population[0][:]
            Bestscore=max(scorefinal)
        
 

        
    