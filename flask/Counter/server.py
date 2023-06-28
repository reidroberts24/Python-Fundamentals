from flask import Flask, render_template, redirect, session, url_for, request

app = Flask(__name__)
app.secret_key = 'myFirstSecretKey'

@app.route('/')

def index():
    session['count'] = session.get('count', 0) +1
    session['visits'] = session.get('visits', 0) + 1
    return render_template('index.html', count=session['count'], visits=session['visits'])


@app.route('/increment', methods=["POST"])
def increment():
    return redirect(url_for('index'))

@app.route('/add_two', methods=["POST"])
def add_two():
    session['count'] += 1
    return redirect(url_for('index'))

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['count'] = -1
    session['visits'] = -1
    return redirect(url_for('index'))

@app.route('/specify_times', methods=['POST'])
def specify_times():
    
    num_times = request.form['specify_times']
    if num_times == '':
        num_times = 0
    else:
        num_times = int(num_times)
    
    session['count'] += num_times
    return redirect(url_for('index'))

# SENSEI BONUS
#import base64
#eyJjb3VudCI6NTAsInZpc2l0cyI6MjZ9
#base64.urlsafe_b64decode('eyJjb3VudCI6NTAsInZpc2l0cyI6MjZ9===')


if __name__ == "__main__":
    app.run(debug=True)
