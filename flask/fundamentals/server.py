from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello/<string:word>/<int:num>')
def hello(word, num):
    return render_template('hello.html', word=word, num=num)
if __name__=="__main__":
    app.run(debug=True)