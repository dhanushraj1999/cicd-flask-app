from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my CI/CD pipeline!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)