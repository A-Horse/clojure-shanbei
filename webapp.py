from flask import Flask, request, send_from_directory
import json

app = Flask('Learn-word',  static_url_path='/static', static_folder='web')

setting = {
    'host': 'localhost'
}


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/egg', methods=['GET'])
def egg():
    return 'Hello World!'


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
    app.run(host=setting['host'], port=7777)
