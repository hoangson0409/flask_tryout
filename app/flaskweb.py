from flask import Flask
from SP.supporting_func import true_hello
app = Flask(__name__)
@app.route("/")
def hello():
    return true_hello()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)