#
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/Sasquatch')
def Welcome():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sighting')
def sighting():
    return render_template('edit.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/show')
def show():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)