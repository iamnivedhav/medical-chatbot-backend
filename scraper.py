import requests
from bs4 import BeautifulSoup
import json

def extract_symptoms_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    symptoms = []

    # Find symptom-related headings or paragraphs
    symptom_triggers = soup.find_all(lambda tag: (
        tag.name in ['h2', 'h3', 'p'] and 'symptom' in tag.get_text(strip=True).lower())
    )

    for trigger in symptom_triggers:
        next_el = trigger.find_next_sibling()
        while next_el:
            if next_el.name in ['h2', 'h3']:  # stop at next section
                break
            if next_el.name == 'ul':
                for li in next_el.find_all('li'):
                    text = li.get_text(strip=True)
                    if text:
                        symptoms.append(text)
            next_el = next_el.find_next_sibling()
        if symptoms:
            break

    return symptoms

# Load the seed list
with open("condition_seed.jsonl", "r") as f:
    condition_seeds = json.load(f)

rag_dataset = []

for item in condition_seeds:
    try:
        print(f"Scraping: {item['title']}")
        r = requests.get(item['url'], timeout=10)
        symptoms = extract_symptoms_from_html(r.text)
        if symptoms:
            rag_dataset.append({
                "title": item['title'],
                "symptoms": symptoms,
                "department": item['department']
            })
        else:
            print(f"❌ Skipped {item['title']} — no symptoms found")
    except Exception as e:
        print(f"❌ Failed to scrape {item['title']}: {e}")

# Save results
with open("rag_dataset.jsonl", "w") as f:
    for entry in rag_dataset:
        f.write(json.dumps(entry) + "\n")
