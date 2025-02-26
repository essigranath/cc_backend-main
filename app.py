from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello")
    return "<h1>Hello World!<h1>"

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data)

    # here be sentiment analysis
    # pickle

    return {'input_data': input_data, 'message': 'hello!'}


if __name__ == '__main__':
    app.run(debug=True)

