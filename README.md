# 🩺 Medical Department Recommendation System (Symptom-based RAG API)

This project is a **Retrieval-Augmented Generation (RAG)-based backend API** that recommends a suitable **medical department** based on user-described symptoms. It uses sentence similarity models and a scraped symptom-disease dataset to make recommendations via a simple Flask API.

---

## 🚀 Features

- Recommends departments like Cardiology, Neurology, Psychiatry, etc., based on symptoms.
- Uses `sentence-transformers` for semantic matching.
- Pre-built RAG dataset with 125 curated entries.
- Flask-based API with OpenAPI spec.
- Hosted on Render.
- Includes scraping tools to build the dataset from:
  - [WHO Disease Fact Sheets](https://www.who.int/news-room/fact-sheets)
  - [MedlinePlus Medical Encyclopedia](https://medlineplus.gov)

---

## 🧠 Workflow

### 1. 🕸️ Web Scraping (`scraper.py`)
- Reads from `condition_seed.jsonl` (title, URL, department).
- Extracts `<li>` items following headings/paragraphs containing the word "symptom".
- Builds a clean `rag_dataset.jsonl` file with:
  ```json
  {
    "title": "Diabetes",
    "symptoms": ["Increased thirst", "Frequent urination", "Fatigue"],
    "department": "General Physician"
  }
  
### 2. 🧠 Symptom Analysis Logic (app.py)
Loads the RAG dataset and precomputes embeddings.
When a user submits symptom text, computes the most semantically similar entry using cosine similarity.
Returns the department linked to the best-matching symptom list.
If symptoms are too general (e.g., fever, stomach pain), defaults to recommending General Physician.

## 🔧 API Usage
### 🔹 Request Body
{
  "symptoms": "I have a cough and chest tightness"
}
### 🔹 Response
{
  "recommended_department": "Pulmonology"
}

## 🛠️ Tech Stack
Python 3.11
Flask
Sentence Transformers (all-MiniLM-L6-v2)
JSONL-based RAG
Hosted on Render (free web service)

## 📁 Project Structure
├── app.py                      # Main Flask API
├── rag_dataset.jsonl           # Final RAG symptom-disease data
├── condition_seed.jsonl        # Input file with disease titles and WHO/Medline links
├── scraper.py                  # Scraping script to build rag_dataset.jsonl
├── requirements.txt            # All required dependencies
├── render.yaml                 # Render deployment config
├── Procfile                    # Required by Render to run the Flask app

## 🌐 Deployment (Render)
This app is deployed on Render. To replicate:
Push all code to a GitHub repository.
Create a new Web Service on Render connected to your repo.

## 🔒 Notes
All scraped data is stored locally; no external API calls during inference.
If a user symptom matches very common ones (e.g., “fever”, “stomach ache”), fallback to General Physician.

## 📜 License
This project is for academic purposes and follows all ethical scraping standards from WHO and MedlinePlus.

## 👩‍💻 Developed by
Nivedha V (Computer Science Engineering)
