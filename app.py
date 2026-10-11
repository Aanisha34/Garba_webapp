from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'Garba.csv')

# CSV file ko load karne ka code (apne anusar yahan DataFrame logic likhein)
# df = pd.read_csv(CSV_PATH)

# ==========================================
# YAHAN ROUTE ADD KARNA ZAROORI HAI:
# ==========================================
@app.route('/')
def home():
    # Yeh aapke 'templates' folder ke andar 'index.html' file ko kholega
    return render_template('index.html')

# Agar aapka koi aur search ya result page bhi hai, toh uska route bhi aise hi banega:
# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     # search logic...
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)