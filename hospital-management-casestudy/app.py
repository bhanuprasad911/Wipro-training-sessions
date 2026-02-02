from flask import Flask, request, jsonify
import json

app  = Flask(__name__)
with open('patients.json', 'r') as p:
    patients_data = json.load(p)

@app.route('/')
def home():
    return 'Hospital management server is live'
#get all patients
@app.route('/patients', methods=["GET"])
def get_all_patients():
    try:
        if len(patients_data)==0:
            return json({"message":"No patients avaliable"}), 200
        return patients_data, 200
    except Exception as e:
        print(e)
        return jsonify({"message":"Error while fetching patients data"}), 500
    

if __name__ == "__main__":
    app.run(debug=True)