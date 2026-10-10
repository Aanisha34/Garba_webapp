from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Yahan file ka naam 'garba.csv' set kar diya hai
FILE_PATH = 'garba.csv'

@app.route('/', methods=['GET', 'POST'])
def home():
    if not os.path.exists(FILE_PATH):
        return f"<h3>Error: '{FILE_PATH}' file nahi mili! Kripya check karein ki file garba_webapp folder me hai ya nahi.</h3>"
    
    df = pd.read_csv(FILE_PATH)
    
    # Search query filter
    search_query = request.args.get('search', '').strip()
    if search_query:
        df = df[df['Guest_Name'].str.contains(search_query, case=False, na=False) | 
                df['Pass_ID'].str.contains(search_query, case=False, na=False)]
    
    # Status filter
    status_filter = request.args.get('status', 'All')
    if status_filter == 'Paid':
        df = df[df['Payment_Status'] == 'Paid']
    elif status_filter == 'Unpaid':
        df = df[df['Payment_Status'] == 'Unpaid']
    elif status_filter == 'Checked In':
        df = df[df['Check_In_Status'] == 'Checked In']

    # Summary Stats
    full_df = pd.read_csv(FILE_PATH)
    total_passes = len(full_df)
    total_revenue = int(full_df['Price_INR'].sum())
    checked_in = len(full_df[full_df['Check_In_Status'] == 'Checked In'])
    
    data = df.to_dict(orient='records')
    
    return render_template('index.html', data=data, total_passes=total_passes, 
                           total_revenue=total_revenue, checked_in=checked_in, 
                           search_query=search_query, status_filter=status_filter)

# Naya Pass Add karne ka Route
@app.route('/add', methods=['POST'])
def add_pass():
    df = pd.read_csv(FILE_PATH)
    
    new_row = {
        'Pass_ID': request.form['pass_id'],
        'Guest_Name': request.form['guest_name'],
        'Contact_Number': request.form['contact'],
        'Pass_Type': request.form['pass_type'],
        'Event_Date': request.form['event_date'],
        'Price_INR': int(request.form['price']),
        'Payment_Status': request.form['payment_status'],
        'Check_In_Status': 'Pending'
    }
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)