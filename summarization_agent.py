import json
from transformers import pipeline

def load_search_results(file_path="search_results.json"):
    """Loads search results from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def summarize_text(text):
    """Uses Pegasus Model for text summarization."""
    summarizer = pipeline("summarization", model="google/pegasus-xsum")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    search_results = load_search_results()

    combined_text = " ".join([result["title"] for result in search_results])
    
    print("\n🔍 Generating Summary...")
    summary = summarize_text(combined_text)

    print("\n📌 **Summary:**")
    print(summary)

    with open("summary.txt", "w") as f:
        f.write(summary)

    print("\n✅ Summary saved in `summary.txt`")
