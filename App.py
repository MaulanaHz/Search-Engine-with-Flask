from flask import Flask, render_template
from query import search

app = Flask(__name__)
app.config["DEBUG"] = True

#route utama
@app.route('/')
def home():
    return render_template('index.html')

#route dari api search
@app.route('/api/<query>/<banyak>')
def api_search(query, banyak):
    return search(query, int(banyak))

app.run()
