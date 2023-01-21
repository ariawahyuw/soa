import numpy as np

title = "Problem 3 Contour Plot"

pi = np.pi
e = np.exp(1)
def f_1(x_1, x_2):
    return np.sin(4*pi*x_1*x_2)-(x_1 + x_2)

def f_2(x_1, x_2):
    return (4-1/(4*pi))*(np.exp(2*x_1)-e)+4*e*x_2**2-2*e*x_1

def f(x):
    return 1/(1+abs(f_1(*x))+abs(f_2(*x)))

d = 1e-2 # the least distance between each variable of roots
num_roots = 10 # number of roots that we want to find
k_max = 150
m = 100
r = 0.95
theta = np.pi/4
x1_lim = [-2, 1]
x2_lim = [-1, 1]
R = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
S_2 = np.dot(np.diag([r,r]), R)