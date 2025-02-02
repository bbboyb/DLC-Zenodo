import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("tennis.csv")
play = data['play']
plt.hist(play)