import numpy as np

title = "Problem 1 Contour Plot"


def f_1(x_1, x_2):
    return np.exp(x_1-x_2) - np.sin(x_1+x_2)

def f_2(x_1, x_2):
    return x_1**2*x_2**2-np.cos(x_1+x_2)
def f(x):
    return 1/(1+abs(f_1(*x))+abs(f_2(*x)))

d = 1e-2 # the least distance between each variable of roots
num_roots = 6 # number of roots that we want to find
k_max = 200
m = 50
r = 0.95
theta = np.pi/4
x1_lim = [-10, 10]
x2_lim = [-10, 10]
R = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
S_2 = np.dot(np.diag([r,r]), R)