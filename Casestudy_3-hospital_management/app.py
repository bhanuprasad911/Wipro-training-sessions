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
            return jsonify({"message":"No patients avaliable"}), 200
        return patients_data, 200
    except Exception as e:
        print(e)
        return jsonify({"message":"Error while fetching patients data"}), 500

@app.route('/patients/<int:patient_id>', methods=["GET"])
def get_patient_by_id(patient_id):
    try:
        for patient in patients_data:
            if patient['id'] == patient_id:
                return jsonify(patient), 200
        return jsonify({"message":"Patient not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message":"Error while fetching patient data"}), 500

@app.route('/patients', methods=["POST"])
def add_patient():
    try:
        new_patient = request.get_json()
        if not new_patient:
            return jsonify({"message":"Input data is empty"}), 400
        required_fields = ("name", "age", "disease", "contact", "doctor_assigned")
        for field in required_fields:
            if field not in new_patient:
                return jsonify({"message": f"Missing required field: {field}"}), 400
        new_id = max([p["id"] for p in patients_data], default=0) + 1
        new_patient["id"] = new_id
        patients_data.append(new_patient)
        with open('patients.json', 'w') as p:
            json.dump(patients_data, p, indent=4)
        return jsonify({"message":"Patient added successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message":"Error while adding patient"}), 500
    
    
@app.route('/patients/<int:patient_id>', methods=["PUT"])
def update_patient(patient_id):
    try:
        update_data = request.get_json()
        if not update_data:
            return jsonify({"message":"Input data is empty"}), 400
        for patient in patients_data:
            if patient['id'] == patient_id:
                patient.update(update_data)
                with open('patients.json', 'w') as p:
                    json.dump(patients_data, p, indent=4)
                return jsonify({"message":"Patient updated successfully"}), 200
        return jsonify({"message":"Patient not found"}), 404
    except Exception as e:
        print(e)
        return jsonify({"message":"Error while updating patient data"}), 500



if __name__ == "__main__":
    app.run(debug=True)