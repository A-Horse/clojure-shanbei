from flask import Flask, request, send_from_directory
import json

from sqlite3 import IntegrityError

import learnword

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
        learnword.add_word(word)
    except NameError:
        return json.dumps({'message': 'Can not query this word.', 'status': 1})
    except IntegrityError:
        return json.dumps({'message': 'Word already exist.', 'status': 1})
    except:
        raise
        return json.dumps({'message': 'Unknown', 'status': 1})


@app.route('/add', methods=['POST'])
def modify_word_status():
    return json.dumps({'message': 'unknown', 'status': 1})


if __name__ == '__main__':
    app.debug = True
    app.run(host=setting['host'], port=7777)
