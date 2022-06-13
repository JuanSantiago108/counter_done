from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route("/")
def homepage():
    # session['number'] = 2
    if 'number' in session:
        session['number'] += 1
    else:
        session['number'] = 0
    return render_template("index.html")

@app.route("/destoy_session")
def destoy_session ():
    session.clear()
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)