import numpy as np
import random 
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys
import time

class Tree:
    def __init__(self,status):
        self.status=status
        self.color=None
    def StatCol(self):
        if self.status==1:
            self.color='g'
            return
        elif self.status==2:
            self.color='y'
            return
        elif self.status==3:
            self.color='r'
            return
        elif self.status==4:
            self.color='b'
            return



class Forest:

    def __init__(self, dim, prob):
        self.dim=dim
        self.prob=prob
        self.forest=np.full((self.dim,self.dim), Tree(0))
        self.t=0
        self.trees=0
        self.burnt=0
        self.burning=0
        self.fig=plt.figure()
        self.ax=self.fig.add_subplot(111)
        #self.fig,self.ax=plt.subplots()
        

    def create_forest(self):
        
        for i in range(len(self.forest)):
            for j in range(len(self.forest[0])):
                if self.prob>=random.uniform(0,1):
                    self.forest[i][j]=Tree(1)
                    self.trees+=1
                else:  
                    self.forest[i][j]=Tree(0)



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

        
    def animate(self):
        x_val=[]
        y_val=[]
        col=[]
        plt.clf()
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.forest[i][j].status!=0:
                    self.forest[i][j].StatCol()
                    if self.forest[i][j].color!='None':
                        col.append(self.forest[i][j].color)
                        x_val.append(i)
                        y_val.append(j)
                   # print(i,j,self.forest[i][j].color)
        plt.scatter(x_val,y_val,c=col)
        plt.pause(0.005)
        
       # plt.show()
        

    def burning_the_whole_sharade(self, animate_for=False):
        self.start_fire()
        if animate_for==True:
            plt.ion()
            self.animate()
            
        while self.burning!=0 and self.burning>0:
            self.burn_timestep()
            if animate_for==True:
                self.animate()
        #plt.show()

        
if __name__=="__main__":
    print('create forest')
    For=Forest(50,0.8)
    For.create_forest()

    print('burn it')
    For.burning_the_whole_sharade(True)
    print('Time before extinction :', For.t)
    print('Total Trees :', For.trees)
    print('Percent burnt :', For.burnt/For.trees)
 
                    

