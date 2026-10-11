from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Aapka baaki code yahan rahega...
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'Garba.csv')

# Yeh line Vercel ke liye zaroori hai (agar local pe run karna ho toh app.run() rakhein)
if __name__ == '__main__':
    app.run(debug=True)