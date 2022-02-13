from shutil import ReadError
from numpy import square
import pandas as Pd
import csv 
import math

with open("data.csv") as f:
   reader = csv.reader(f)
   filedata = list(reader)
data = filedata[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+= int(x)
    mean = total/n
    return mean
squarelist = []
for number in data :
    a = int(number) - mean(data)
    a = a**2
    squarelist.append(8)
sum = 0
for i in squarelist: 
    sum = sum+ i
result = sum / (len(data)-1)
standardd = math.sqrt(result)
print(standardd)