from math import pi
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,2*(np.pi),0.1)
type(x)
y=np.sin(x)
plt.plot(x, y) 
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show() 