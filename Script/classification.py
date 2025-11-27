#!/usr/bin/env python3
"""
classification.py

Load vessel shape scores from Excel, classify each vessel as 'round' or 'oblique'
based on a threshold, and plot the distribution of these classes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the Excel file containing your vessel shape scores
FILE_PATH = os.path.join(
    os.path.expanduser('~'),
    'ThesProj',
    'Bhautik_Poshiya',
    'nnunet_bhautik',
    'Script',
    'vessel_shape_scores.xlsx'
)

# Threshold above which vessels are considered "round"
SHAPE_THRESHOLD = 0.9

def main():
    # 1) Load the Excel data into a DataFrame
    df = pd.read_excel("/Users/bhautikposhiya/Downloads/vessel_shape_scores.xlsx")
    
    # 2) Print the first few rows for sanity check
    print("\n=== Vessel Shape Scores (first 5 rows) ===")
    print(df.head(), "\n")
    
    # 3) Classify each vessel by mean_shape_score
    df['shape_class'] = df['mean_shape_score'].apply(
        lambda x: 'round' if x >= SHAPE_THRESHOLD else 'oblique'
    )
    
    # 4) Show the counts of each class
    counts = (
        df['shape_class']
        .value_counts()
        .rename_axis('Shape Class')
        .reset_index(name='Count')
    )
    print("=== Shape Class Counts ===")
    print(counts, "\n")
    
    # 5) Plot the distribution as a bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(counts['Shape Class'], counts['Count'])
    plt.xlabel('Shape Class')
    plt.ylabel('Number of Vessels')
    plt.title(f'Distribution of Vessel Shape Classes (threshold = {SHAPE_THRESHOLD})')
    plt.tight_layout()
    
    # 6) Save the figure
    out_png = 'vessel_shape_distribution.png'
    plt.savefig(out_png)
    print(f"Saved bar chart to {out_png}")
    
    # 7) Also show it interactively if you like
    plt.show()

if __name__ == '__main__':
    main()