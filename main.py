from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/inicio')
def inicio():
    return render_template('index.html')



app.run()