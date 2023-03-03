import numpy as np
import time
from matplotlib import use
from problems.problem3 import x1_lim, x2_lim, \
                              f_1, f_2, f, \
                              k_max, m, S_2, \
                              d, num_roots, \
                              title    
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from scipy.stats import qmc, norm

def random_generator(m, x1_boundary, x2_boundary, d=2):
    sampler = qmc.Sobol(d)
    sample = sampler.random_base2(int(np.log2(m)))
    lb = [x1_boundary[0], x2_boundary[0]]
    ub = [x1_boundary[1], x2_boundary[1]]
    return qmc.scale(sample, lb, ub)

use("Agg")
x_1 = np.linspace(*x1_lim, 500)
x_2 = np.linspace(*x2_lim, 500)
a, b = np.meshgrid(x_1, x_2)
fig, ax = plt.subplots(1,1, figsize=(7,7))
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_title(title)
ax.contour(a, b, f_1(a,b), [0], colors='b')
ax.contour(a, b, f_2(a,b), [0], colors='k')
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
movie_writer = FFMpegWriter(fps=15, metadata=metadata)
x = random_generator(m, x1_lim, x2_lim)
x_star = x[np.argmax(f(x.T))]
mark = ax.scatter(*x.T, marker="X", color="red")
with movie_writer.saving(fig, 'myfile_5.mp4', dpi=150):
    for _ in range(k_max):
        x = np.dot(S_2,x.T).T - np.dot((S_2 - np.diag([1,1])), x_star)
        # mask are indexes of x which lies in the domain
        mask = np.where((x[:,0] >= x1_lim[0]) & (x[:,0] <= x1_lim[1])
                        & (x[:,1] >= x2_lim[0]) & (x[:, 1] <= x2_lim[1]))
        # select only x that lies in the domain
        x_def = x[mask]
        #print(x_def.shape)
        x_def_T = x_def.T
        x_def_1, x_def_2 = x_def_T
        mark.set_offsets(np.c_[x_def_1, x_def_2])
        movie_writer.grab_frame()
        x_star = x_def[np.argmax(f(x_def.T))]

print(f"Roots: \n{x_star}")