import matplotlib
import sys
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



print(matplotlib.__version__)

#I actually donno why, but executing this file on ubuntu python3 
# yiedls some really wierd stuffs

# after visually selecting a couple of line like this, press 
#: and write-->norm .
#
#get used to using period frequently
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
#var = 'i want a cat';
