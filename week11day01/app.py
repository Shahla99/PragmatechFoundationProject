from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/about')
def about():
    return 'Flask yükləndi'

if __name__=='__main__':
    app.run(debug=True)