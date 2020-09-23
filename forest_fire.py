import numpy as np
import random 
import matplotlib.pyplot as plt
import sys

class Tree:
    def __init__(self,status):
        self.status=status
    



class Forest:

    def __init__(self, dim, prob):
        self.dim=dim
        self.prob=prob
        self.forest=np.full((dim,dim), Tree)
        self.t=0
        self.trees=0
        self.burnt=0
        self.burning=0
       

    def create_forest(self):
        
        for i in range(len(self.forest)):
            for j in range(len(self.forest[0])):
                if self.prob>=random.uniform(0,1):
                    self.forest[i][j]=Tree(1)
                    self.trees+=1
                else:  
                    self.forest[i][j]=Tree(0)


    def show(self):
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==1:
                    plt.plot(i,j, 'go')
                if self.forest[i][j].status==2:
                    plt.plot(i,j, 'yo')
                if self.forest[i][j].status==3:
                    plt.plot(i,j, 'ro')
        plt.show()

    def start_fire(self):
        for i in range(len(self.forest)):
                if self.forest[i][-1].status==1:
                    self.forest[i][-1].status=2
                    self.burning+=1
                    

    def burn_neighbor(self,i,j):
        if j-1>0 and self.forest[i][j-1].status==1:
            self.forest[i][j-1].status=1.5
            self.burning+=1

        if j+1<len(self.forest) and self.forest[i][j+1].status==1:
            self.forest[i][j+1].status=1.5
            self.burning+=1
   
        if i+1<len(self.forest[0]) and self.forest[i+1][j].status==1:
            self.forest[i+1][j].status=1.5
            self.burning+=1

        
        if i-1>0 and self.forest[i-1][j].status==1:
            self.forest[i-1][j].status=1.5
            self.burning+=1

        
        self.forest[i][j].status=3
        self.burnt+=1
        self.burning-=1

    def set_ablaze(self):
        for i in range(len(self.forest[0])):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==1.5:
                    self.forest[i][j].status=2


    def burn_timestep(self):
        self.set_ablaze()
        for i in range(len(self.forest[0])):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==2:
                    self.burn_neighbor(i,j)
        self.t+=1
    

    def burning_the_whole_sharade(self):
        self.start_fire()
        while self.burning!=0:
            self.burn_timestep()


"""  For=Forest(50,0.6)
For.create_forest()
For.start_fire()
For.burning_the_whole_sharade()
For.show()"""
                    

