from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return "hello 劳伦士"


if __name__ == '__main__':
    app.run()
