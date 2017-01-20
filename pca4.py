import numpy as np
import matplotlib.pyplot as plt

# Euler ODE method
# INPUTS:
#       x0 - initial position
#       v0 - initial velocity
#       ti - start time
#       tf - stop time
#       dt - time step
# OUTPUTS:
#       position(x), velocity(v), and time(t)
def euler(x0,v0,ti,tf,dt):
    print("in euler!")
    # time, position, and velocity arrays
    t = np.arange(ti,tf,dt)
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0

    for i in range(len(t)-1):
        x[i+1] = x[i] + v[i]*dt
        v[i+1] = v[i] - x[i]*dt # there is a hidden (k/m) = (1/1) in front of the x[i]dt term

    return x,v,t

# Prediction Correction Method
#      - same inputs and outputs as Euler
def predi_corr(x0,v0,ti,tf,dt):
    t = np.arange(ti,tf,dt)
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = x0
    v[0] = v0

    for i in range(len(t)-1):
        #Euler
        x[i+1] = x[i] + v[i]*dt
        v[i+1] = v[i] - x[i]*dt

        #correction
        x[i+1] = x[i] + (v[i] + v[i+1])*dt/2.0
        v[i+1] = v[i] - (x[i] + x[i+1])*dt/2.0
    return x,v,t

def epsilon(x,v,t):
    e0 = 0.5*np.power(v[0],2.0) + 0.5*np.power(x[0],2.0)
    ef = 0.5*np.power(v[len(t)-1],2.0) + 0.5*np.power(x[len(t)-1],2.0)
    return np.fabs(ef - e0)/e0
