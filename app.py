import os
import pandas as pd

# Yeh code automatic exact path dhoond leta hai chahe aap local PC par ho ya Vercel par
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(BASE_DIR, 'garba.csv')

df = pd.read_csv(csv_path)