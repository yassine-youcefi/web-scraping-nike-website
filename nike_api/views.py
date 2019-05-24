from run import app

from flask import jsonify,render_template

@app.route('/')
def home():
    return render_template('index.html')

app.run(port= 4848) 