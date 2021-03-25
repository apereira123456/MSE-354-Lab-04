import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-354-Lab-04\Data.csv')

angle_deg = data.iloc[:, 0]
power = data.iloc[:, 1]

power_max = max(power)

X = np.sin(np.pi * angle_deg / 180)
Y = power / power_max *100

fig = plt.figure(dpi=300)
plt.plot(X, Y, linestyle='--', marker='o')
    
plt.title('Numerical Aperture Determination')
plt.xlabel(r'$\sin{(\theta)}$ (arb. unit)')
plt.ylabel(r'Accepted Power (%)')
plt.yscale("log")

fig.savefig('plot.png')