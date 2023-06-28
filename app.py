from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route('/img')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'img'), filename)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)