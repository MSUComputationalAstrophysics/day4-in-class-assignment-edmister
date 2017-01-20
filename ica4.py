import matplotlib.pyplot as plt
import numpy as np
from pca4 import euler
from pca4 import epsilon

def euler_crom(x0,v0,ti,tf,dt):
    print("in euler_crom!")
    # time, position, and velocity arrays
    t = np.arange(ti,tf,dt)
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0

    for i in range(len(t)-1):
        v[i+1] = v[i] - x[i]*dt
        x[i+1] = x[i] + v[i+1]*dt # there is a hidden (k/m) = (1/1) in front of the x[i]dt term

    return x,v,t



def runga_kutta4(x0,v0,ti,tf,dt):
    print("in runga_kutta4!")
    t = np.arange(ti,tf,dt)
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0

    for i in range(len(t)-1):
        x1 = x[i]
        v1 = v[i]
        a1 = -x1

        x2 = x1 + v1*dt/2.0
        v2 = v1 + a1*dt/2.0
        a2 = -x2

        x3 = x1 + v2*dt/2.0
        v3 = v1 + a2*dt/2.0
        a3 = -x3

        x4 = x1 + v3*dt
        v4 = v1 + a3*dt
        a4 = -x4

        x[i+1] = x[i] + dt*(v1 + 2.0*v2 + 2.0*v3 + v4)/6.0
        v[i+1] = v[i] + dt*(a1 + 2.0*a2 + 2.0*a3 + a4)/6.0
    return x,v,t

def epsilon_check(x0,v0,ti,tf,dt,f):
    eps = 0
    n = 0
    while eps < 1e-4:
        print('dt = ',dt)
        sol = f(x0,v0,ti,tf,dt)
        eps = epsilon(sol[0],sol[1],sol[2])
        print("epsilon = ",eps)
        if eps < 1e-4:
            dt *=1.001

    return tf/dt

q1 = euler(0,1,0,4*np.pi,0.1*np.pi)
q2 = euler(0,1,0,4*np.pi,0.01*np.pi)
q3 = euler(0,1,0,4*np.pi,0.001*np.pi)

p1 = euler_crom(0,1,0,4*np.pi,0.1*np.pi)
p2 = euler_crom(0,1,0,4*np.pi,0.01*np.pi)
p3 = euler_crom(0,1,0,4*np.pi,0.001*np.pi)

run1 = runga_kutta4(0,1,0,4*np.pi,0.1*np.pi)
run2 = runga_kutta4(0,1,0,4*np.pi,0.01*np.pi)
run3 = runga_kutta4(0,1,0,4*np.pi,0.001*np.pi)

t = [0.1*np.pi,0.01*np.pi,0.001*np.pi]

eps_run = [epsilon(run1[0],run1[1],run1[2]), epsilon(run2[0],run2[1],run2[2]), epsilon(run3[0],run3[1],run3[2])]
eps_eu = [epsilon(q1[0],q1[1],q1[2]), epsilon(q2[0],q2[1],q2[2]), epsilon(q3[0],q3[1],q3[2])]
eps_euc = [epsilon(p1[0],p1[1],p1[2]), epsilon(p2[0],p2[1],p2[2]), epsilon(p3[0],p3[1],p3[2])]

plt.figure(111)
plt.plot(t,eps_run,marker='o',linewidth=3)
plt.plot(t,eps_eu,marker='s',linewidth=3)
plt.plot(t,eps_euc,marker='^',linewidth=3)
plt.yscale('log')
plt.xlabel('dt')
plt.ylabel(r'$\epsilon$')
plt.legend(['RK4','Euler','Euler-Cromer'],loc='best')
plt.savefig('epsilon.png',dpi=600)


# Calculate the number of steps for each function to reach epsilon greater than 10-4
print("steps = ",epsilon_check(0,1,0,4*np.pi,0.000001*np.pi,euler))
