import numpy as np
import matplotlib.pyplot as plt
def EstimatingVelocity(givenStepSize):
    """
    givenStepSize -> a Number that interval  givenStepSize > 0
        default  = 1
    """
    lastVelocity =  0
    initalTime = 0
    gravity = 9.81
    velocities = {}
    velocities[initalTime] = 0
    for step in np.arange(givenStepSize,9,givenStepSize): 
        if (step > 8):
            break
        lastVelocity = lastVelocity + (gravity - ((12.5/68.1)*lastVelocity))*givenStepSize
        velocities[step] = lastVelocity

    return velocities


velocitiesFirst = EstimatingVelocity(1) # for step size is 1
velocitiesSecond = EstimatingVelocity(0.5) # for step size 0.5
figure1 , axs  = plt.subplots(2)
figure1.suptitle('Graph of Velocities')

axs[0].plot(list(velocitiesFirst.keys()),list(velocitiesFirst.values()),label='Step for 1')
axs[0].legend()
axs[0].grid(True)
axs[1].plot(list(velocitiesSecond.keys()),list(velocitiesSecond.values()),label='Step for 0.5',color='red')
axs[1].legend()
axs[1].grid(True)
plt.xlabel("Time(t)")
plt.ylabel("Velocity(m/s)")
plt.show()