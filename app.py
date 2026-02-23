import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/components")
def components():
    return render_template("components.html")

@app.route('/googlea6b3d7e05c3d84a1.html')
def google_verification():
    return send_from_directory('.', 'googlea6b3d7e05c3d84a1.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)