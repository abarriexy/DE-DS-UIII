# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:00:53 2026

@author: Taufik Sutanto
"""

# climate_analysis.py
import pandas as pd
from modularLib import dataPreprocessing
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("raw_data.csv")

df = dataPreprocessing(df)

# 3. Plot
plt.plot(df['date'], df['temperature'])
plt.show()