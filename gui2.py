import matplotlib.pyplot as plt
import numpy as np

x = np.array([2011,2012,2013,2014,2015,2016])
y= np.array([12,52,13,63,24,75])

figure, axis = plt.subplots(2,2)
axis[0,0].plot(x,y)

a = [2011,2012,2013,2014,2015]
b = [21,19,24,17]

axis[0,1].scatter(x,y)
plt.show()