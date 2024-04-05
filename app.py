from flask import Flask, render_template
import sqlite3
import datetime 

app = Flask(__name__)

# Connects to db and pulls in data for the dashboard
def get_latest_metrics():
    conn = sqlite3.connect('system_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM metrics ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()

    return row

@app.route('/')
def dashboard():
    metrics = get_latest_metrics()
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(debug=True) 
