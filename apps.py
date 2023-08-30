from apps import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/whoami')
def whoami():
    return 'I am James McKeown'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')