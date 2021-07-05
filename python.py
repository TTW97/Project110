import plotly.figure_factory as ff 
import csv
import statistics
import pandas as pd 
import random

df = pd.read_csv('newdata.csv')
data = df["average"].tolist()
population_mean = statistics.mean(data)

fig = ff.create_distplot([data], ["average"], show_hist = False)
fig.show()





