import numpy as np

title = "Problem 2 Contour Plot"

def f_1(x_1, x_2):
    return 0.5*np.sin(x_1*x_2) - 0.25*x_2/np.pi - 0.5*x_1

def f_2(x_1, x_2):
    return (1-0.25/np.pi)*(np.exp(2*x_1)-np.exp(1))+np.exp(1)*x_2/np.pi - 2*np.exp(1)*x_1
def f(x):
    return 1/(1+abs(f_1(*x))+abs(f_2(*x)))

d = 1e-1 # the least distance between each variable of roots
num_roots = 12 # number of roots that we want to find
k_max = 100
m = 400
r = 0.95
theta = np.pi/4
x1_lim = [-0.5, 2]
x2_lim = [-17, 4]
R = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
S_2 = np.dot(np.diag([r,r]), R)