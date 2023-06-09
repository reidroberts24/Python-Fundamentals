from flask import *
import random

app = Flask(__name__)
app.secret_key = 'ZAePMPlj61'


#app generates new number each refresh so I will redirect to other templates when the user is guessing
@app.route('/')
def index():
    random_num = session['rand_num'] = random.randint(1,100)      
    print(session['rand_num']) 
    return render_template('index.html')



################################# main method for the user to guess #################################
@app.route('/guess', methods=['POST'])
def guess():
    session['user_guess'] = request.form.get('user_guess')
    hint = ""

    try:        
        int(session['user_guess'])      # need to account for people not putting numbers
        session['is_int'] = True
    except:
        session['is_int'] = False
        return redirect(url_for('keep_guessing'))
    session['user_guess'] = int(session['user_guess'])

    if session['user_guess'] == session['rand_num']: #if correct guess, redirect to correct webpage
        return redirect(url_for('correct_answer'))

    return redirect(url_for('keep_guessing')) #otherwise redirect to keep guessing

#renders the new template for being right
@app.route('/correct_answer')
def correct_answer():
    return render_template('correct.html')

#renders the new template for being wrong
@app.route('/keep_guessing')
def keep_guessing():
    hint = ""
    if 'is_int' in session:
        if session['is_int'] == False:
            hint = "Enter an integer!"
        else:
            if session['user_guess'] > session['rand_num']:
                hint = "Too high!"
            else:
                hint = "Too low!"
    return render_template('wrong.html', hint=hint)

#simply redirects back to the index function to start over
@app.route('/play_again', methods=['POST'])
def play_again():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)