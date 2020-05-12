from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return "hello 劳伦士"

@app.route('/contact')
def contact():
    html = '''
    联系我
    '''
    return html
if __name__ == '__main__':
    app.run(debug=True)
