from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def survey():

    if request.method == 'POST':
        print(request.form)


    return render_template("survey.html")


if __name__ == "__main__":
    app.run(debug=True)