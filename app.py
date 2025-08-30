from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello santosh kumar i successfuly deployed project on cloud."

if __name__ == "__main__":
    # Container ko alive rakhne ke liye Flask server run karenge
    app.run(host="0.0.0.0", port=5000)
