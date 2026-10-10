import os
import pandas as pd

# Absolute path set karne ke liye taaki Vercel par bhi file mil jaye
basedir = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(basedir, 'garba.csv')

# Ab pandas se file aise read karein:
df = pd.read_csv(csv_path)