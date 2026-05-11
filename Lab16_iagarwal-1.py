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


