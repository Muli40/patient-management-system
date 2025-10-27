from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    patient_id = request.form['patient-id']
    full_name = request.form['full-name']
    dob = request.form['dob']
    gender = request.form['gender']
    admission_date = request.form['admission-date']
    ward_bed = request.form['ward-bed']
    admitting_reason = request.form['admitting-reason']

    # For now, just return details (later you can save to DB)
    return f"""
    <h2>Patient Saved!</h2>
    <p><b>ID:</b> {patient_id}</p>
    <p><b>Name:</b> {full_name}</p>
    <p><b>DOB:</b> {dob}</p>
    <p><b>Gender:</b> {gender}</p>
    <p><b>Admission Date:</b> {admission_date}</p>
    <p><b>Ward/Bed:</b> {ward_bed}</p>
    <p><b>Reason:</b> {admitting_reason}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)