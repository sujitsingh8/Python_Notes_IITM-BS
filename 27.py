import matplotlib.pyplot as plt
import numpy as np

# -------- First subplot --------

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,1)
plt.plot(x,y)

# -------- Second subplot --------

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,3,2)
plt.plot(x,y)

# -------- Third subplot --------

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,3)
plt.plot(x,y)

# -------- Fourth subplot (position 4 is skipped) --------
''' Note: subplot(2,3,4) is NOT used here,
    so this position will remain empty '''

# -------- Fifth subplot --------

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,3,5)
plt.plot(x,y)

# -------- Sixth subplot --------

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()