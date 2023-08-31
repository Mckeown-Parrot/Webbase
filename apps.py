#from apps import Flask
from flask import Flask
from flask import render_template

app = Flask(__name__, )

@app.route('/')
def index():
    return render_templates('index.html')

@app.route('/whoami')
def whoami():
    return 'I am James McKeown'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8181)