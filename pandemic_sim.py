import numpy as np
import random 
import matplotlib.pyplot as plt
import sys


class pathogen:

    pass

class person:
    def __init__(self):
        self.infected=0
        self.pathogens=[]
        self.current_pathogen=None
        self.mut_prob=0
        self.recovery_chance=0.6
        self.reinfection_chance=0

    def infect(self,pathogen):
        if pathogen in self.pathogens:
            self.current_pathogen=pathogen
            if self.reinfection_chance< random.uniform(0,1):
                self.mutate(self.mut_prob)
                self.infected=1
        else:
            self.pathogens.append(pathogen)
            self.current_pathogen=pathogen
            if self.reinfection_chance< random.uniform(0,1):
                self.infected=1
    
    def recover(self):
        if self.recovery_chance<random.uniform(0,1):
            self.infected=0
            self.current_pathogen=None
            return -1
        else:
            return 0

    def mutate(self, mut_prob):
        if mut_prob>random.uniform(0,1) and self.current_pathogen!=None and self.infect!=0:
            self.current_pathogen=pathogen()
            self.pathogens.append(self.current_pathogen)




class population:
    def __init__(self, size, p,q):
        self.dim=size
        self.p=p
        self.q=q
        self.population=np.full((self.dim,self.dim), person())
        self.total_infected=0
        self.t=0
        self.infection_prob=0.02


    def create_population(self):
                
        for i in range(len(self.population)):
            for j in range(len(self.population[0])):
                self.population[i][j]=person()

    def show_infection(self,fig=plt,show=True):
        for i in range(len(self.population)):
            for j in range(len(self.population[0])):
              #  print(self.population[i][j].infected)
                if self.population[i][j].infected==1:
                    plt.plot(i,j,'ro')
                
                if self.population[i][j].infected==2:
                     plt.plot(i,j,'r*')
             
                if self.population[i][j].infected==0:
                    plt.plot(i,j,'go')

        if show==True:
            fig.show()


    def spread_individual(self,x,y):
        neighbours=[-1,1]
        pathogen=self.population[x][y].current_pathogen
        for i in range(len(neighbours)):
            if self.dim<=x+neighbours[i]:
                self.population[0][y].infect(pathogen)
                continue
            elif  x+neighbours[i]<0:
                self.population[-1][y].infect(pathogen)
                continue
            elif self.population[x+neighbours[i]][y].infected==0:
                self.population[x+neighbours[i]][y].infect(pathogen)
                continue

        for j in range(len(neighbours)):
            if self.dim<=x+neighbours[j]:
                self.population[x][0].infect(pathogen)
            elif  x+neighbours[j]<0:
                self.population[x][-1].infect(pathogen)

            elif self.population[x][y+neighbours[j]].infected==0:
                self.population[x][y+neighbours[j]].infect(pathogen)


    
    
    def spread_across(self):
        for i in range(len(self.population)):
            for j in range(len(self.population)):
               if self.population[i][j].infected==2:
                   self.spread_individual(i,j)

    def manifest_infection(self):
        for i in range(len(self.population)):
            for j in range(len(self.population[0])):
                if self.population[i][j].infected==1:
                    self.population[i][j].infected=2
                    self.total_infected+=1



    def create_patient_zero(self):
        pathogenOG=pathogen()
        while self.total_infected==0:
            for i in range(len(self.population)):
                for j in range(len(self.population[0])):
                    if self.infection_prob>=random.uniform(0,1):
                        self.population[i][j].pathogen=pathogenOG
                        self.population[i][j].infected=2
                        self.total_infected+=1
                        print('infected')

    

    def recover(self):
        for i in range(len(self.population)):
            for j in range(len(self.population[0])):
                self.total_infected+=self.population[i][j].recover()
                print(self.total_infected)
    


    def infection_timestep(self):
        self.spread_across()
        self.recover()
        self.t+=1
        
    def infection_run_til_cured(self):
        self.create_patient_zero()
        while self.total_infected!=0:
            self.infection_timestep()
            print(self.t)

    


if __name__=="__main__":
    pop=population(20,0,0)
    pop.create_population()
    pop.infection_run_til_cured()
    pop.show_infection()