
import requests
import json

YoudaoApiKey = '711979406'
YoudaoKeyFrom = 'learn-english-cfw'
YoudaoApi = 'http://fanyi.youdao.com/openapi.do?keyfrom=' + YoudaoKeyFrom \
            + '&key=' + YoudaoApiKey + '&type=data&doctype=json&version=1.1&q='


def query_youdao(word):
    r = requests.get(YoudaoApi + word)
    jsonDate = json.loads(r.text)
    print jsonDate

ShanbeiWordApi = 'https://api.shanbay.com/bdc/search/?word='


def query_shanbei_word(word):
    r = requests.get(ShanbeiWordApi + word)
    jsonData = json.loads(r.text)
    data = jsonData['data']
    pronunciations = 'us:' + data['pronunciations']['us'] + ' '\
                     'uk:' + data['pronunciations']['uk']
    definition = data['definition']
    audio = data['audio']
    shanbay_id = data['id']
    return definition, shanbay_id, audio, pronunciations



query_shanbei_word('word')


