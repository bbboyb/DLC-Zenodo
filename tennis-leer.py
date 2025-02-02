import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("tennis.csv")
play = data['play']
plt.hist(play)
plt.title("Play tennis")
plt.xlabel("Play?")
plt.ylabel("Frecuencia")
plt.savefig("histograma_play.png")