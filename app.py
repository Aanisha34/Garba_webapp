import os
import pandas as pd

# Path set karte waqt 'Garba.csv' (Capital G) likhein
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'Garba.csv')

# Agar error message me bhi dikhana ho, toh yehi path use karein:
if not os.path.exists(CSV_PATH):
    # Error message ko bhi update kar sakte hain
    pass

df = pd.read_csv(CSV_PATH)