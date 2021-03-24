import matplotlib.pyplot as plt
import numpy as np
def tankProblem(tStart = 0 , tEnd = 10 , tStep = 0.5):
    import math
    A = 1250
    Q = 450
    CalculatedY = 0
    tAndYvalues = {}
    tAndYvalues[tStart] = 0
    for steps in np.arange(tStart+tStep, tEnd , tStep):
        interval = steps-tStep
        CalculatedY = CalculatedY + ((3*Q/A*math.pow(math.sin(interval),2))-Q/A)*tStep
        tAndYvalues[steps] = CalculatedY
    return tAndYvalues

tankProblems = tankProblem()
print(tankProblems)
plt.plot(list(tankProblems.keys()),list(tankProblems.values()),label="Water Level")
plt.xlabel("Time(t)")
plt.ylabel("Level(m)")
plt.legend()
plt.grid(True)
plt.show()