#Roger Chess
#2-19-2021
#github.com/Roger0-0
import numpy as np
import matplotlib.pyplot as plt

###Constants#########################################
#Simpson's Rule parameters, itterations, lower bound,
#upper bound, step width.
N=1000
a=0
b=np.pi
h=(b-a)/N
#M parameters, determines how many bessel functions 
#are plotted.
MinM=0
MaxM=2
#X parameters, min,max, steps
#(higher for smoother plot, lower for faster run time.)
MinX=0
MaxX=20
steps=200
#####################################################

#calls functions and appends answers dictionary
#to bessels dictionary to eventually plot the 
#data on the last line of the function.
def main():
    bessels={}
    for m in range(MinM,MaxM+1):
        answers={"x":[],"y":[]}
        for x in np.linspace(MinX,MaxX,steps):
            answer=simp(m,x)
            answers["y"].append(answer)
            answers["x"].append(x)
        bessels["J{}".format(m)]=answers

    plot(bessels)

#plots data from nested dictonary.
def plot(bessels):
    for i in range(MinM,MaxM+1):
        plt.plot(bessels["J{}".format(i)]["x"],#plots xvals of Jm
                bessels["J{}".format(i)]["y"],#plots yvals of Jm
                label=r"$J_{}(x)$".format(i))#labels Jm for legend
    plt.legend()
    plt.xlabel("x",size=15)
    plt.ylabel(r"$J_m(x)$",size=15)
    plt.title(r"$J_m(x)$ vs x",size=25)
    plt.show()

#Computes Simpsons Rule
def simp(m,x):
    odds=[]
    evens=[]
    for k in range(1,N,2):
        odd=4*func(m,x,a+k*h)
        odds.append(odd)
    for k in range(2,N,2):
        even=2*func(m,x,a+k*h)
        evens.append(even)

    return h/3*(func(m,x,a)+func(m,x,b)+sum(odds)+sum(evens))

#Computes Bessel function for one instance. 
def func(m,x,theta):
    return (1/np.pi)*np.cos(m*theta-x*np.sin(theta))



main()
