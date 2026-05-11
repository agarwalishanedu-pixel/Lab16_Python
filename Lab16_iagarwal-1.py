"""
Program Name: Lab 16
My name: Ishan Agarwal
Purpose: This program is meant to help understand how CSV files are read and used.
Starter Code: None
Date: 05/10/2026
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding ='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, col_title in enumerate(header_row):
    print(f"{index}: {col_title}", end=' ')
print()

#creates the lists for data
dates = []
unemp_rates = []

#Fills the data
for row in reader:
    try:
        curr_date = datetime.strptime(row[0], '%Y-%m-%d')
        curr_rate = float(row[1])
    except ValueError as e:
        print(curr_date)
    else:
        dates.append(curr_date)
        unemp_rates.append(curr_rate)

#graphing processed data
figure, graph = plt.subplots()

graph.plot(dates, unemp_rates, color='blue')

#formatting graph
graph.set_title("Ohio Unemployment (by Month): 1976-2022", fontsize= 24)
graph.set_ylabel("Unemp Rate", fontsize= 16)
graph.set_xlabel("Date", fontsize= 16)
figure.autofmt_xdate()

#creates the file for the graph
plt.savefig ("ohio_unemployment.png", bbox_inches = 'tight', pad_inches = 0.5)
plt.show()