import os
import json
from flask import Flask, jsonify, request
from ptstemmer.implementations.OrengoStemmer import OrengoStemmer
from ptstemmer.implementations.SavoyStemmer import SavoyStemmer
from ptstemmer.implementations.PorterStemmer import PorterStemmer

app = Flask(__name__)
stemmer = OrengoStemmer() 
stemmer.enableCaching(1000) #Optional

@app.route('/')
def main():
    return   '''
            <html>
                <head><title>Stemming Words</title></head>
                <body>
                <p>
                    <h3>Rotas</h3>
                    <ul>
                        <li>/steam?word=digite_a_palavra_desejada</li>
                    </ul>
                </p>
                </body>
            </html>
            '''
@app.route('/steam')
def get_steam_by_word():
    steam = { 'steam': stemmer.getWordStem(request.args.get('word')) }
    return json.dumps(steam, ensure_ascii=False).encode('utf8')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)