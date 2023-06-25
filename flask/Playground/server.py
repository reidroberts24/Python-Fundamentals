from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def display_3_boxes():
    return render_template('index.html')

@app.route('/play/<int:num_times>')
def display_x_boxes(num_times):
    return render_template('index.html',num_times=num_times)

@app.route('/play/<int:num_times>/<string:color>')
def display_x_boxes_in_color(num_times,color):
    return render_template('index.html',num_times=num_times, color=color)

if __name__=="__main__":
    app.run(debug=True)