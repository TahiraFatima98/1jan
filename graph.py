from math import pi
import matplotlib.pyplot as plot
import numpy as np
time= np.arange(0, 10, 0.1);
amplitude=np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show() 