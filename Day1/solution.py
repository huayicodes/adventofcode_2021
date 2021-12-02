import pandas as pd 

"""
Part 1
"""
# read in the input 
input_df = pd.read_csv("Day1/input.txt", header = None)

def ct_increase(input_df):
    return (input_df.diff()>0).sum()

print(ct_increase(input_df))

"""
Part 2
"""
def ct_3_slide(input_df):
    return ct_increase(input_df.rolling(3).sum())

print(ct_3_slide(input_df))