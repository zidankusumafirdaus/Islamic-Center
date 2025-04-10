from flask import Flask, render_template

app = Flask(__name__)

global appType 

appType = 'Islamic Center'

@app.route('/')
def index():
    return render_template('dashboard.html', appType=appType)

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        debug = 'True'
        )