from flask import Flask, render_template
import requests

request = requests.get("https://catfact.ninja/fact")

request = request.json()

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', data=request)

if __name__=="__main__":
    app.run(debug=True)
