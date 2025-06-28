from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if _name_ == "_main_":
    app.run(debug=True)