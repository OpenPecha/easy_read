from flask import Flask
from flask import render_template, request, send_file
from botok import WordTokenizer
from botok.config import Config
from pathlib import Path

app = Flask(__name__)

def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False)
    return tokens

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tokenize', methods=['post'])
def tokenize():
    config = Config(dialect_name='general', base_path=Path.home())
    wt= WordTokenizer(config=config)
    input_text = request.form['ipText']
    tokens = get_tokens(wt, input_text)
    ouput_text = "".join([str(token) for token in tokens])
    return render_template('index.html',input_text=input_text,output = ouput_text)


@app.route('/download_token',methods=['post'])
def download_token():
    output_text = request.form['opText']
    with open('output.txt', 'w', encoding='utf-8') as file:
              file.write(output_text) 
    return send_file('output.txt', as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
