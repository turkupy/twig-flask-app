from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/", methods=["POST"])
def get_city():
    if request.method == "POST":
        city = request.form["text"]
        return city

@app.route("/magda")
def magda():
    return "Hello...?"


if __name__ == "__main__":
    app.run(debug=True)