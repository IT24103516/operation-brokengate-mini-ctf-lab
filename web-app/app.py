from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/robots.txt")
def robots():
    return """User-agent: *
Disallow: /backup
"""

@app.route("/backup")
def backup():
    return """
    Backup Notes:
    Internal account: analyst
    Hint: Check the source carefully.
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)