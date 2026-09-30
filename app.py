"""
AI Lotto Smart App

Statistical analysis and weighted number generation
based on historical lottery draws.

Note: Lottery draws are independent random events.
No statistical model can predict future draws.
This tool is for data exploration and education only.
"""

import pandas as pd
import random
from collections import Counter


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

DATA_FILE = "lotto_data.csv"
MAX_NUMBER = 50
PICK_COUNT = 6
OVERDUE_BONUS = 0.5
NUM_SETS = 3

# ---------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------

def load_data(path=DATA_FILE):
    """Read historical draws from CSV and sort by date."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    ball_cols = [c for c in df.columns if c.startswith("num")]
    if len(ball_cols) != 6:
        raise ValueError("CSV must contain columns num1 through num6")

    return df

# --------------------------------------------------------------------- 
# Analysis 
# --------------------------------------------------------------------- 
 
def compute_frequency(df, max_number=MAX_NUMBER): 
    """Count appearances of each number across all draws.""" 
    ball_cols = [c for c in df.columns if c.startswith("num")] 
    values = df[ball_cols].values.flatten().tolist() 
 
    freq = Counter(values) 
    for n in range(1, max_number + 1): 
        freq.setdefault(n, 0) 
 
    return dict(freq) 
 
 
def compute_overdue(df, max_number=MAX_NUMBER): 
    """Count draws since each number last appeared.""" 
    ball_cols = [c for c in df.columns if c.startswith("num")] 
 
    total = len(df) 
    overdue = {} 
 
    for n in range(1, max_number + 1): 
        last_index = -1 
        for idx, row in df.iterrows(): 
            if n in row[ball_cols].values: 
                last_index = idx 
        overdue[n] = total if last_index == -1 else total - 1 - last_index 
 
    return overdue 
 
 
def rank_numbers(freq, top=5): 
    """Return the most and least frequent numbers.""" 
    ordered = sorted(freq.items(), key=lambda item: item[1], reverse=True) 
    hot = ordered[:top] 
    cold = ordered[-top:] 
    return hot, cold