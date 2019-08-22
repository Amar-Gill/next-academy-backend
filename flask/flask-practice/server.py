from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    signed_in = False
    first_name = request.args.get('first_name')
    return render_template('index.html', signed_in=signed_in, first_name=first_name)

@app.route('/user/<username>')
def show_username(username):
    return f"Hi {username}"

@app.route('/contact')
def contact():
    signed_in = False
    return render_template('contact.html', signed_in=signed_in)

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run(debug=True)
