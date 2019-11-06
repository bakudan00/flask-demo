from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # signed_in = True
    first_name = request.args.get("first_name")
    return render_template('index.html')

@app.route('/contact')
def contact():
    # signed_in = True
    return render_template('contact.html')

if __name__ == '__main__':
   app.run()