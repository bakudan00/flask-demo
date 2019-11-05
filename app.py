from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)

@app.route('/Home')
def home():
    return 'Hello Hello Im back'

if __name__ == '__main__':
   app.run(debug=True)