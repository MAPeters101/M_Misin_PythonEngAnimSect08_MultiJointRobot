import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0=0
t_end=1
dt=0.005
t=np.arange(t0,t_end+dt,dt)

# Joint 1
r1=3+t
f1=1
alpha1=2*np.pi*f1*t
x1=(r1)*np.cos(alpha1)
y1=(r1)*np.sin(alpha1)

# Joint 2
r2=2
f2=1
alpha2=2*np.pi*f2*t # With respect to the 1st joint
dx1=(r2)*np.cos(alpha2+alpha1)
dy1=(r2)*np.sin(alpha2+alpha1)
x2=x1+dx1
y2=y1+dy1

############################## ANIMATION ##############################





