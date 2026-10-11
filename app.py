from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'Garba.csv')

@app.route('/')
def home():
    # CSV file read karna
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
    else:
        df = pd.DataFrame(columns=['Pass_ID', 'Guest_Name', 'Contact_Number', 'Pass_Type', 'Event_Date', 'Price_INR', 'Payment_Status', 'Check_In_Status'])
    
    # Search aur Filter logic
    search_query = request.args.get('search', '').strip()
    status_filter = request.args.get('status', 'All')
    
    if search_query:
        df = df[df['Guest_Name'].astype(str).str.contains(search_query, case=False, na=False) | 
                df['Pass_ID'].astype(str).str.contains(search_query, case=False, na=False)]
                
    if status_filter == 'Paid':
        df = df[df['Payment_Status'] == 'Paid']
    elif status_filter == 'Unpaid':
        df = df[df['Payment_Status'] != 'Paid']
    elif status_filter == 'Checked In':
        df = df[df['Check_In_Status'] == 'Checked In']
        
    # Stats calculate karna jo HTML me dikh rahe hain
    total_passes = len(df)
    total_revenue = int(df['Price_INR'].sum()) if 'Price_INR' in df.columns and not df.empty else 0
    checked_in = len(df[df['Check_In_Status'] == 'Checked In']) if 'Check_In_Status' in df.columns and not df.empty else 0
    
    data = df.to_dict(orient='records')
    
    return render_template('index.html', 
                           data=data, 
                           total_passes=total_passes, 
                           total_revenue=total_revenue, 
                           checked_in=checked_in,
                           search_query=search_query,
                           status_filter=status_filter)

@app.route('/add', methods=['POST'])
def add_pass():
    # Naya pass add karne ka logic yahan aayega
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)