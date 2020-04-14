from flask  import Flask,render_template,redirect,url_for
app=Flask(__name__)

posts=[
    {'author'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("xyz.html")


@app.route("/about")
def about():
    return render_template('xyz.html')

if __name__== "__main__" :
    app.run(debug=True)