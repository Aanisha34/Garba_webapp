import os
import pandas as pd

# Multi-location fallback logic for Vercel serverless environment
base_dir = os.path.dirname(os.path.abspath(__file__))

# Possible locations where Vercel might place the file
possible_paths = [
    os.path.join(base_dir, 'Garba.csv'),
    os.path.join(base_dir, 'garba.csv'),
    os.path.join(os.getcwd(), 'Garba.csv'),
    os.path.join(os.getcwd(), 'garba.csv'),
    'Garba.csv',
    'garba.csv'
]

csv_path = None
for path in possible_paths:
    if os.path.exists(path):
        csv_path = path
        break

if csv_path is None:
    raise FileNotFoundError("Error: 'Garba.csv' file kisi bhi expected path par nahi mili!")

df = pd.read_csv(csv_path)