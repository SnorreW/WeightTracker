import matplotlib.pyplot as plt
import pandas as pd

#Reads the file where the weights are
df = pd.read_csv("vekt.csv")
#Creates a simple moving average
df['SMA'] = df["0"].rolling(window=7).mean()
#Displays the plot
plt.plot(df)
plt.show()
