from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import json
import os

# Initialize Flask app
app = Flask(__name__)

# Load the RAG dataset
with open("rag_dataset.jsonl", "r", encoding="utf-8") as f:
    rag_data = [json.loads(line) for line in f]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Pre-compute RAG embeddings
rag_embeddings = model.encode(
    ["; ".join(entry["symptoms"]) for entry in rag_data],
    convert_to_tensor=True
)

# Inference logic
def recommend_department(user_input):
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, rag_embeddings)[0]
    best_match_index = int(similarities.argmax())
    best_entry = rag_data[best_match_index]
    return best_entry["department"]

# API endpoint
@app.route("/analyze_symptoms", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        symptoms_text = data.get("symptoms", "").strip()

        if not symptoms_text:
            return jsonify({"department": "General Physician"}), 200

        department = recommend_department(symptoms_text)
        return jsonify({"department": department}), 200

    except Exception as e:
        return jsonify({"department": "General Physician"}), 200

# For local testing or Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
