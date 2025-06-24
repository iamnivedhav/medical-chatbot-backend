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
    try:
        data = request.get_json(force=True)
        user_symptoms = data.get("symptoms", "").lower()

        for keyword, department in knowledge_base.items():
            if keyword in user_symptoms:
                return jsonify({"department": department}), 200
        
        # Default fallback department
        return jsonify({"department": "General Physician"}), 200

    except Exception as e:
        # Always return valid JSON even on backend errors
        return jsonify({"department": "General Physician"}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
