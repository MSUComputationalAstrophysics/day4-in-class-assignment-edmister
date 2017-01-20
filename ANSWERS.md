I plotted both the RK4 and Euler-Cromer methods. Both methods show superior conservation of energy over the basic Euler method. The Euler-Cromer is approximately 100 times better than the basic Euler Method, while the RK4 method is approximately a million times better (and even better at the shortest time step)

####Energy Conservation
![Figure 1](epsilon.png?)

####How many steps to 0.01%?
In order to find the number of steps for each method, I iteratively called the method with a small enough dt (informed by the energy conservation figure) and increased the time step slowly. Once the method crossed 0.01% threshold, I calculated the number of steps by finding 4$\pi$/dt. In order to find the number of floating point operations, I multiplied the number of steps by the number of operations per iteration (RK4:~55?,Euler-Cromer:4,Euler:4)

RK4: 56 steps, ~ 3000 floating point operations

Euler-Cromer: 1235 steps, ~ 5000 floating point operations

Euler: ~ 1,600,000steps, ~ 6,400,000floating point operations

It's obvious that the RK4 method shines above the rest in precision, time steps taken, and floating point operations needed, in order to solve the calculation.