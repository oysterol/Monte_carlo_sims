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
        self.forest=np.full((self.dim,self.dim), Tree(0))
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


    def show(self,fig=plt, show=True):
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==1:
                    fig.plot(i,j, 'go')
                if self.forest[i][j].status==2:
                    fig.plot(i,j, 'yo')
                if self.forest[i][j].status==3:
                    fig.plot(i,j, 'ro')
                if self.forest[i][j].status==4:
                    fig.plot(i,j, 'bo')
        if show==True:
            fig.show()

    def start_fire(self):
        for i in range(len(self.forest)):
                if self.forest[i][-1].status==1:
                    self.forest[i][-1].status=2
                    self.burning+=1
                    

    def burn_neighbor(self,i,j):
        if j-1>=0 and self.forest[i][j-1].status==1:
            self.forest[i][j-1].status=1.5
            self.burning+=1

        if j+1<len(self.forest) and self.forest[i][j+1].status==1:
            self.forest[i][j+1].status=1.5
            self.burning+=1
   
        if i+1<len(self.forest[0]) and self.forest[i+1][j].status==1:
            self.forest[i+1][j].status=1.5
            self.burning+=1

        
        if i-1>=0 and self.forest[i-1][j].status==1:
            self.forest[i-1][j].status=1.5
            self.burning+=1
        
        self.forest[i][j].status=3
 
    def set_ablaze_and_extinguish(self):
        for i in range(len(self.forest[0])):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==1.5:
                    self.forest[i][j].status=2
                if self.forest[i][j].status==3:
                    self.forest[i][j].status=4
                    self.burning-=1
                    self.burnt+=1


    def burn_timestep(self):
               
        self.set_ablaze_and_extinguish()
        
        for i in range(len(self.forest[0])):
            for j in range(len(self.forest)):
                if self.forest[i][j].status==2:
                    self.burn_neighbor(i,j)

        self.t+=1
    

    def burning_the_whole_sharade(self, animate=False):
        self.start_fire()
        if animate==True:
            fig=plt.figure()
            ax = fig.add_subplot(111)
                

        while self.burning!=0 and self.burning>0:

            self.burn_timestep()
            if animate==True:
                self.show()

if __name__=="__main__":
    print('create forest')
    For=Forest(50,0.8)
    For.create_forest()
    print('burn it')
    For.burning_the_whole_sharade()
    For.show()
    print('Time before extinction :', For.t)
    print('Total Trees :', For.trees)
    print('Percent burnt :', For.burnt/For.trees)

                    

