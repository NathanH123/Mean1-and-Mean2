import pandas as pd
import csv
import plotly.express as px

with open("class1.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
totalmarks = 0
totalentry = len(filedata)
for marks in filedata:
    totalmarks+= float(marks[1])
mean = totalmarks/ totalentry
print(mean)
df = pd.read_csv("class1.csv")
figure = px.scatter(df,x="Student Number", y= "Marks")
figure.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean, y1 = mean,
        x0 = 0, x1 = totalentry,
    )
])
figure.update_yaxes(rangemode = "tozero")
figure.show()