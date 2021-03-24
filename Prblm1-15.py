
import matplotlib.pyplot as plt
import numpy as np

def forCircuit(): # Q 1.15
    forT = [i for i in np.arange(0,0.11,0.01)]
    i = [0]
    q = [1]
    for varK in range(1,11):
        i.append(i[varK-1]-(i[varK-1]*200+q[varK-1]/0.0001)/5 *0.01)
        q.append(q[varK-1]+i[varK-1]*0.01)
    return forT , i , q

t , i , q  = forCircuit()
plt.suptitle('I and Q versus T')
plt.plot(t,i,label='I')
plt.plot(t,q,label='Q')
plt.legend()
plt.xlabel("Time(t)")
plt.grid(True)
plt.show()
