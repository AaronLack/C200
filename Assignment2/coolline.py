#All Work Here is Solely Mine!

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervalse
x = np.arange(0., 10.0, 0.2)

#red dashes
plt.plot(x, x**2 + 2*x + 2, 'g--')
plt.plot(x, x**3, 'r^')
plt.plot(x, x*4 - 3, 'b')
plt.plot(x, 6*x**2 + 5*x + 1, 'o')
plt.xlabel("My Inputs")
plt.ylabel("My Outputs")
plt.title("Best Graph")
plt.show()


#What does he mean by "Change the program to say Best Graph?" Clarify
