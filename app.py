from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello dear, missing Tanvir? <br>He is busy with creating His personal website.</p><br><br><h1>কাঠ গোলাপের সাদার মায়া মিশিয়ে দিয়ে ভাবি <br>আবছা নীল তোমার লাগে ভালো।</h1>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)