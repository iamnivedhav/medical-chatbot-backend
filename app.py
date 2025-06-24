from flask import Flask, request, jsonify

app = Flask(__name__)

knowledge_base = {
    "chest pain": "Cardiology",
    "breathlessness": "Cardiology",
    "palpitations": "Cardiology",
    "rash": "Dermatology",
    "itching": "Dermatology",
    "redness": "Dermatology",
    "headache": "Neurology",
    "seizures": "Neurology",
    "numbness": "Neurology",
    "abdominal pain": "Gastroenterology",
    "bloating": "Gastroenterology",
    "back pain": "Orthopedics",
    "joint stiffness": "Orthopedics",
    "cough": "Pulmonology",
    "wheezing": "Pulmonology",
    "shortness of breath": "Pulmonology",
    "sore throat": "ENT",
    "ear pain": "ENT",
    "blurry vision": "Ophthalmology",
    "eye pain": "Ophthalmology",
    "depression": "Psychiatry",
    "anxiety": "Psychiatry"
}

@app.route('/analyze_symptoms', methods=['POST'])
def analyze_symptoms():
    data = request.get_json()
    user_symptoms = data.get("symptoms", "").lower()

    for keyword, department in knowledge_base.items():
        if keyword in user_symptoms:
            return jsonify({"department": department})
    
    return jsonify({"department": "General Physician"})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
