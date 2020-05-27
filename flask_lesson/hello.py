from flask import Flask, render_template
from models.book import Book

app = Flask(__name__)

@app.route('/')
def cao():
    return render_template('index.html')

@app.route('/books/')
def book_list():
    books = [Book('Python flask',59.00,'wg','人民币'),
            Book('fuck',38.00,'wg','人民币'),
            Book('多线程',59.00,'wg','人民币'),
            Book('hua',23.00,'wg','人民币')
            ]
    return render_template('book-list.html',books=books)

@app.route('/hello')
def index():
    return "hello 劳伦士"

@app.route('/contact/')
def contact():
    html = '''
    联系我
    '''
    return html
if __name__ == '__main__':
    app.run(debug=True)
