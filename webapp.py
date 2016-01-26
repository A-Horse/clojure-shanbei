from flask import Flask, request, send_from_directory
import json

app = Flask('Learn-word')

setting = {
    'host': 'localhost'
}

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/add', methods=['POST'])
def add_word():
    try:
        print request.form
    except:
        return json.dumps({'error': 'unknown'})

if __name__ == '__main__':
    app.debug = True
    app.run(setting['host'])
