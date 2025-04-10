from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://api.alquran.cloud/v1"

@app.route('/dashboard')
def index():
    return render_template('dashboard.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/surah', methods=['POST'])
def get_surah():
    surah_number = request.form.get('surah_number')
    response = requests.get(f"{API_URL}/surah/{surah_number}")
    data = response.json()
    return render_template('index.html', surah=data['data'])

if __name__ == '__main__':
    app.run(debug=True)