"""
Simple app to solve wordle puzzle
CITATION: The above dataset is from Donald E. 
Knuth who is a Professor Emeritus of The Art of
Computer Programming at Stanford University.

"""
import pandas as pd
from pyparsing import Regex

df = pd.read_csv('database.txt', header=None)


mask = df[df[0].str.contains(r'^(?!.*a)ra[a-b|d-m|o-z]e$')]

print(mask)