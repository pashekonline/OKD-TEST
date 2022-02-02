from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return jsonify({"message":"Hello, World!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
