from duckduckgo_search import DDGS
import json

def search_web(query, num_results=5):
    """Searches DuckDuckGo and returns top results."""
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=num_results))
    return results

if __name__ == "__main__":
    topic = input("Enter a topic to research: ")
    search_results = search_web(topic)
    
    # Print and Save Results
    print("\nSearch Results:")
    for idx, result in enumerate(search_results):
        print(f"{idx+1}. {result['title']} - {result['href']}")
    
    with open("search_results.json", "w") as f:
        json.dump(search_results, f, indent=4)

    print("\nSearch results saved in search_results.json")
