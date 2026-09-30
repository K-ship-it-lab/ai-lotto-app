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
