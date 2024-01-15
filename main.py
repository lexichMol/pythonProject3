from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def registration():
    if (request.form.get("I") != None or request.form.get("T") != None) and request.form.get("name") != None:

        return redirect(url_for("task"))
    print(request.form.get("name"))
    print(request.form.get("I"))
    print(request.form.get("T"))
    return render_template("index.html")

@app.route("/task", methods=['GET', "POST"])
def task():

    if request.form.get("intest1") == "10" and request.form.get("intest2") == "5":
        return redirect(url_for("ok"))
    elif request.form.get("intest1") != None and request.form.get("intest2") != None:
        return redirect(url_for("no"))

    return render_template("task.html")

@app.route("/ok")
def ok():
    return render_template("ok.html")

@app.route("/no")
def no():
    return render_template("no.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)