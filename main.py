# my name is Anthony O'Neal and this is my work
# Lorenz attractor code for Project 7

import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from scipy.integrate import odeint

#Part 1 Code----------------------------------------------------------------------------------
Sval = float(input("Input the value of Prandtl's number sigma: \n> "))
Rval = int(input("Input the value of Rayleigh's number r:  \n> ")) # getting user input
Bval = float(input("Input the value of Reynold's number beta:  \n> "))

#save current value for plot titles
def lorenz(x, y, z, s=Sval, r=Rval, b=Bval):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = x*(r-z)-y
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def xdot(x,y):
    return 10*(y - x)


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor; s =" + str(Sval)+ ",r =" + str(Rval) + ",b =" + str(Bval))
plt.show()

#plot for each of the of the x,y, and z variables for every step
ts = np.linspace(0,10001,10001)

plt.plot(ts, xs)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("x(t); s =" + str(Sval)+ ",r =" + str(Rval) + ",b =" + str(Bval))
plt.show()

plt.plot(ts,ys)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("y(t); s =" + str(Sval)+ ",r =" + str(Rval) + ",b =" + str(Bval))
plt.show()

plt.plot(ts,zs)
plt.xlabel("t")
plt.ylabel("z(t)")
plt.title("z(t); s =" + str(Sval)+ ",r =" + str(Rval) + ",b =" + str(Bval))
plt.show()
#------------------------------------------------------------------------------

#Part 2 code-------------------------------------------------------------------

# Arrival time as a function of service start time
startTime = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
plt.scatter(startTime, range(1, 16))
plt.xlabel('Start Time')
plt.ylabel('Arrival Time')
plt.title('Arrival Time vs Start Time')
plt.show()

# Arrival time as a function of exit time
exitTime = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]
plt.scatter(exitTime, range(1, 16))
plt.xlabel('Exit Time')
plt.ylabel('Arrival Time')
plt.title('Arrival Time vs Exit Time')
plt.show()

# Arrival time as a function of time in queue
timeInQ = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]
plt.scatter(timeInQ, range(1, 16))
plt.xlabel('Time in Queue')
plt.ylabel('Arrival Time')
plt.title('Arrival Time vs Time in Queue')
plt.show()

# Arrival time as a function of number of customers in system
customersInSys = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
plt.scatter(customersInSys, range(1, 16))
plt.xlabel('# of Customers in System')
plt.ylabel('Arrival Time')
plt.title('Arrival time vs # of Customers in System')
plt.show()

# Arrival time as a function of number of customers in queue
customersInQ = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]
plt.scatter(customersInQ, range(1, 16))
plt.xlabel('# of Customers in Queue')
plt.ylabel('Customer Arrival Time')
plt.title('Arrival time vs # of Customers in Queue')
plt.show()


#Part 2 number 3
lam = 0.8 # arrival rate
mu = 0.3 # service rate
kArr = [] # factor
uti = [] # utilization
through = [] # throughput
numJob = [0] # number of jobs in system
timeSys = [] # time in system

for k in range(1,100):
    kArr.append(k)
    uti.append((k*lam)/(k*mu))
    through.append(k*mu)
    timeSys.append(-1/(k*(mu-lam)))

#calulate mean number of jobs
for k in range(1,99):
    numJob.append(k*uti[k]/(1-uti[k]))

fig_a, ax_a = plt.subplots()
ax_a.plot(kArr, uti)
ax_a.set_title("a")
ax_a.set_xlabel("k value")
ax_a.set_ylabel("utilization")
plt.show()

fig_b, ax_b = plt.subplots()
ax_b.plot(kArr, through)
ax_b.set_title("b")
ax_b.set_xlabel("k value")
ax_b.set_ylabel("Throughput")
plt.show()

fig_c, ax_c = plt.subplots()
ax_c.plot(kArr, numJob)
ax_c.set_title("c")
ax_c.set_xlabel("k value")
ax_c.set_ylabel("mean number in system")
plt.show()

fig_d, ax_d = plt.subplots()
ax_d.plot(kArr, timeSys)
ax_d.set_title("d")
ax_d.set_xlabel("k")
ax_d.set_ylabel("mean time in system")
plt.show()
