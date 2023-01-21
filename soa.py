import numpy as np
import time
from problems.problem2 import x1_lim, x2_lim, \
                              f_1, f_2, f, \
                              k_max, m, S_2, \
                              d, num_roots, \
                              title    

roots = []
f_root = [] # array to store f1, f2, and f value of roots
iteration = 0
start_time = time.time_ns() // 1_000_000

while len(roots) < num_roots:
    iteration += 1
    # initialize m random points that lies in the domain
    x = np.array([np.array([
            np.random.uniform(low=x1_lim[0], high=x1_lim[1]),
            np.random.uniform(low=x2_lim[0], high=x2_lim[1])])
            for _ in range(m)])
    x_star = x[np.argmax(f(x.T))]
    for _ in range(k_max):
        x = np.dot(S_2,x.T).T - np.dot((S_2 - np.diag([1,1])), x_star)
        # mask are indexes of x which lies in the domain
        mask = np.where((x[:,0] >= x1_lim[0]) & (x[:,0] <= x1_lim[1])
                        & (x[:,1] >= x2_lim[0]) & (x[:, 1] <= x2_lim[1]))
        # select only x that lies in the domain
        x_def = x[mask]
        x_star = x_def[np.argmax(f(x_def.T))]
    # check if roots array is still empty
    if len(roots) == 0:
        roots = np.array([x_star])
        continue
    for i, root in enumerate(roots):
        # check if x_star already in array (with error of epsilon) 
        if np.all(np.isclose(x_star, root, atol=d, rtol=0)):
            break
        # x_star is not in the root and i is the last index of roots array 
        elif i == roots.shape[0] - 1:
            roots = np.append(roots, [x_star], axis=0)
    
end_time = time.time_ns() // 1_000_000
print(f"Roots: \n{roots}")
print(f"Number of iteration to find all roots: {iteration}")
for root in roots: f_root.append([f_1(*root), f_2(*root), f(root)])
print("f1, f2, and merit function value:")
for f_val in f_root: print(f_val)
print(f"Execution time for {iteration} iterations: {end_time-start_time}ms")
