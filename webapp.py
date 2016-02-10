from flask import Flask, request, send_from_directory
import json

from sqlite3 import IntegrityError

import learnword

learnword.reset_learning_word_status()


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


@app.route('/word', methods=['POST'])
def add_word():
    try:
        word = request.form['word']
        learnword.add_word(word)
        return json.dumps({
            'status': 0,
            'message': 'Added successfully!'
        })
    except NameError:
        return json.dumps({'message': 'Can not query this word.', 'status': 1})
    except IntegrityError:
        return json.dumps({'message': 'Word already exist.', 'status': 1})
    except:
        raise
        return json.dumps({'message': 'Unknown', 'status': 1})


@app.route('/word', methods=['PUT'])
def modify_learning_word_status():
    word = request.form['word']
    learnword.learnword


@app.route('/word', methods=['GET'])
def get_learning_word():
    try:
        word = learnword.get_learning_word()
        if word:
            return json.dumps({
                'status': 0,
                'word': {
                    'word': word[0],
                    'shanbay_id': word[1],
                    'definition': word[2],
                    'learn_time': word[3],
                    'status': word[4],
                    'add_date': word[5],
                    'last_learn_date': word[6],
                    'audio': word[7],
                    'pronunciations': word[8]
                }
            })
        else:
            return json.dumps({
                'status': 1,
                'message': 'congratulations, No word should learn.!'
            })
    except:
        raise
    return json.dumps({'message': 'unknown', 'status': 1})


if __name__ == '__main__':
    app.debug = True
    app.run(host=setting['host'], port=7777)
