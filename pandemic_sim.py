import numpy as np
import random 
import matplotlib.pyplot as plt
import sys


class pathogen:

    pass

class person:
    def __init__(self,infected):
        self.infected=infected
        self.pathogens=[]
        self.current_pathogen=None
        self.mut_prob=0
        self.recovery_chance=0.6
        self.reinfection_chance=0

    def infect(self,pathogen):
        if pathogen in self.pathogens:
            self.current_pathogen=pathogen
            if pathogen.reinfection_chance< random.uniform(0,1):
                self.mutate(self.mut_prob)
                self.infected=1
        else:
            self.pathogens.append(pathogen)
            self.current_pathogen=pathogen
            if pathogen.reinfection_chance< random.uniform(0,1):
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
        self.population=np.full((self.dim,self.dim), person)
        self.total_infected=0
        self.t=0
        self.infection_prob=0.02


    def create_population(self,size):
                
        for i in range(len(self.population)):
            for j in range(len(self.population[0])):
                self.population[i][j]=person(0)

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
            if self.dim<x+neighbours[i]:
                self.population[0][y].infect(pathogen)
            elif  x+neighbours[i]<0:
                self.population[-1][y].infect(pathogen)

            elif self.population[x+neighbours][y]==0:
                self.population[x+neighbours][y].infect(pathogen)

        for j in range(len(neighbours)):
            if self.dim<x+neighbours[j]:
                self.population[x][0].infect(pathogen)
            elif  x+neighbours[j]<0:
                self.population[x][-1].infect(pathogen)

            elif self.create_population[x][y+neighbours[j]].person.infected==0:
                self.population[x][y+neighbours[j]].person.infect(pathogen)


    
    
    def spread_across(self):
        for i in range(len(self.dim)):
            for j in range(len(self.dim[0])):
               if self.population[i][j].person.infected==2:
                   self.spread_individual(i,j)

    def manifest_infection(self):
        for i in range(len(self.dim)):
            for j in range(len(self.dim)):
                if self.population[i][j].person.infected==1:
                    self.population[i][j].person.infected=2
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
        for i in range(len(self.dim)):
            for j in range(len(self.dim[0])):
                total_infected+=self.population[i][j].person.recover()
    


    def infection_timestep(self):
        self.spread_across()
        self.recover()
        
    

pop=population(10,0,0)

pop.show_infection()
pop.create_patient_zero()
pop.show_infection()
