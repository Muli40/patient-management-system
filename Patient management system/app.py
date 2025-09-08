from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (for demo purposes)
patients = []

@app.route("/")
def index():
    return render_template("index.html", patients=patients)

@app.route("/add", methods=["POST"])
def add_patient():
    name = request.form.get("name")
    age = request.form.get("age")
    condition = request.form.get("condition")
    if name and age and condition:
        patients.append({"name": name, "age": age, "condition": condition})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)