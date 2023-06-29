from flask import *

app = Flask(__name__)
app.secret_key = 'N5wY4j465vafs4s'

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
    

@app.route('/process', methods=['POST'])
def process():
    
    #joining strings from checkboxes so it doesn't display as a list
    fave_topics = request.form.getlist('topics')
    fave_topics = ', '.join(fave_topics)
    
    #for loop to copy all form data into session dictionary
    for key, val in request.form.items():
        session[key] = val

    loc = session['dojo_location']
    name = session['student_name']
    lang = session['fave_language']
    comments = session['comments']
    experience = session['experience'] #getting radio button info 
    

    return render_template('result.html', stu_name=name, location=loc, comments=comments, fave_lang=lang, fave_topics=fave_topics, experience=experience)

if __name__ == "__main__":
    app.run(debug=True)

