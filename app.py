from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello")
    return "<h1>Hello World version 3!<h1>"

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data)

    # here be sentiment analysis
    # pickle

    return {'input_data': input_data, 'message': 'hello!'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)

