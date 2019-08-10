from flask import Flask, request, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'codingmirchi'

@app.route('/form')
def form():
    return render_template('/form.html')

if __name__ == '__main__':
    app.run(debug=True)