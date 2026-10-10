import os
import pandas as pd

# Yeh code automatic exact path nikal leta hai
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'garba.csv')

# Ab file ko is variable se read karein
df = pd.read_csv(CSV_PATH)