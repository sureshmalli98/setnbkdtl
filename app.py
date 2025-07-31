from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bank_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aadhar TEXT,
            mobile TEXT,
            email TEXT,
            upi TEXT,
            acc_name TEXT,
            ifsc TEXT,
            acc_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = (
        request.form['aadhar'],
        request.form['mobile'],
        request.form['email'],
        request.form['upi'],
        request.form['acc_name'],
        request.form['ifsc'],
        request.form['acc_number']
    )
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bank_details 
        (aadhar, mobile, email, upi, acc_name, ifsc, acc_number)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

    return "<h3>Your details have been submitted successfully!</h3>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
