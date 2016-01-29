from flask import Flask, request
import json

<<<<<<< HEAD
import learnword

app = Flask('Learn-word')
=======
app = Flask('Learn-word',  static_url_path='/static', static_folder='web')
>>>>>>> aaae4552bbb0189e09eb6097a52574850dcbf827

setting = {
    'host': 'localhost'
}


<<<<<<< HEAD
@app.route('/')
=======
@app.route('/', methods=['GET'])
>>>>>>> aaae4552bbb0189e09eb6097a52574850dcbf827
def root():
    return app.send_static_file('index.html')


<<<<<<< HEAD
=======
@app.route('/egg', methods=['GET'])
def egg():
    return 'Hello World!'


>>>>>>> aaae4552bbb0189e09eb6097a52574850dcbf827
@app.route('/add', methods=['POST'])
def add_word():
    try:
        word = request.form['word']
        print word
        print request.form
        return 'hi'
    except:
        return json.dumps({'error': 'unknown'})


if __name__ == '__main__':
    app.debug = True
<<<<<<< HEAD
    app.run(setting['host'])
    
=======
    app.run(host=setting['host'], port=7777)
>>>>>>> aaae4552bbb0189e09eb6097a52574850dcbf827
