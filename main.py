
from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {'saying': 'Fair dinkum', 'translation': 'Really, truly'},
    {'saying': 'She'll be right, mate', 'translation': 'It'll be okay, friend'},
    {'saying': 'No worries', 'translation': 'Don't worry about it'},
    {'saying': 'Chuck a shrimp on the barbie', 'translation': 'Have a barbecue'}
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/translate', methods=['POST'])
def translate():
    saying = request.form['saying']
    translation = translate_to_dutch(saying)
    return render_template('result.html', translation=translation)

def translate_to_dutch(saying):
    # Placeholder function that will actually use a translation API
    return saying.upper()

if __name__ == '__main__':
    app.run(debug=True)
