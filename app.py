from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Why so easy</h1>'

@app.route('/Home')
def home():
    return 'Hello Hello Im back'

if __name__ == '__main__':
   app.run(debug=True)