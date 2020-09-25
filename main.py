
from forest_fire import Forest
import numpy as np
import sys
import matplotlib.pyplot as plt
from pandemic_sim import population

def Montecarlo_forest_fire(F_size,p_steps):
    p=np.linspace(0,1,p_steps)
    burnt=[]
    t_avg=[]
    mont_size=F_size**2


    sys.stdout.write("[%s]" % (" " * len(p)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(p)+1)) 
    for i in range(len(p)):
        prob=0
        t_a=0
        for m in range(mont_size):
            For=Forest(F_size,p[i])
            For.create_forest()
            For.burning_the_whole_sharade()
            if For.trees!=0:
                prob+=For.burnt/For.trees
            t_a+=For.t

            del For
        sys.stdout.write("-")
        sys.stdout.flush()

        burnt.append(prob/mont_size)
        t_avg.append(t_a/mont_size)
    
    
    plt.plot(p,burnt)
    plt.show()
    plt.plot(p,t_avg)
    plt.show()

def Montecarlo_pandemic(size, p_steps, ri_chance, mut_prob):
    p=np.linspace(0,1,p_steps)
    t_avg=[]
    mont_size=size**2


    sys.stdout.write("[%s]" % (" " * len(p)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(p)+1)) 
   


Montecarlo_forest_fire(50,20)
