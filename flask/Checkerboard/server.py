from flask import Flask, render_template
app = Flask(__name__)

rows = 8
cols = 8

@app.route('/')
def index():
    return render_template('index.html', rows=rows, cols=cols)

@app.route('/<int:rows>')
def define_rows(rows):
    rows = rows
    return render_template('index.html', rows=rows, cols=cols)

@app.route('/<int:rows>/<int:cols>')
def define_rows_and_cols(rows, cols):
    rows = rows
    cols = cols
    return render_template('index.html', rows=rows, cols=cols)


if __name__ == "__main__":
    app.run(debug=True)