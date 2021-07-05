import plotly.figure_factory as ff 
import pandas as pd 
import statistics 
import random
import csv

df = pd.read_csv("height-weight-copy.csv")
data = df["Weight(Pounds)"].tolist()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
population_mode = statistics.mode(data)
population_median = statistics.median(data)

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print(mean)
print(std_deviation)