

from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host = '0.0.0.0', port = 5432)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
	app.run(debug=True)
