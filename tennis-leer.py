import pandas as pd
data = pd.read_csv("tennis.csv")
data.to_csv("tennis.csv", index=False)