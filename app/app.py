from flask import Flask, render_template
import requests

request_json = requests.get("https://haveibeenpwned.com/api/v2/breaches")
request = request_json.json()
print (request_json.status_code)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', data=request)

if __name__=="__main__":
    app.run()
