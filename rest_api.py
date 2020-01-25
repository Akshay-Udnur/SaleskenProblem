from flask import Flask, request
from problem_statement_2 import *

app = Flask(__name__)

@app.route('/test', methods = ['GET'])
def test_server():
    return "server is running."

@app.route('/get-similar-sent', methods = ['GET', 'POST']) 
def sent_result():
    input_list = request.get_json()['list_of_sentences']
    return str(main(input_list))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 8000)

