# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:02:03 2026

@author: Taufik Sutanto
"""
import pandas as pd

def dataPreprocessing(df):
    """
    this description of the function
    """
    # 2. Clean Data (The logic is "stuck" here)
    df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
    df['date'] = pd.to_datetime(df['date'])
    return df