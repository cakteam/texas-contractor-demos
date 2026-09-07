import subprocess
import re
import json
import urllib.parse

def search_bing_chrome(query, num_results=10):
    encoded_q = urllib.parse.quote(query)
    url = f"https://www.bing.com/search?q={encoded_q}"
    chrome_cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--dump-dom",
        url
    ]
    try:
        proc = subprocess.run(chrome_cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", timeout=20)
        html_doc = proc.stdout
        # parse bing results
        matches = re.findall(r'<h2[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html_doc)
        results = []
        for href, title in matches:
            clean_title = re.sub(r'<[^>]+>', '', title).strip()
            if "bing.com" not in href and "microsoft.com" not in href and clean_title:
                results.append({"title": clean_title, "url": href})
            if len(results) >= num_results:
                break
        return results
    except Exception as e:
        print(f"Error executing chrome for query '{query}': {e}")
        return []

if __name__ == "__main__":
    queries = [
        "roofing contractors Fort Worth TX reviews",
        "HVAC AC repair Plano TX reviews",
        "garage door repair Arlington TX reviews",
        "emergency plumbing Irving TX reviews",
        "tree removal arborist Fort Worth TX reviews",
        "water damage restoration Dallas TX reviews",
        "foundation repair Arlington TX reviews"
    ]
    all_data = {}
    for q in queries:
        print(f"Searching Bing via Headless Chrome: {q}...")
        res = search_bing_chrome(q, num_results=8)
        all_data[q] = res
        print(f"Found {len(res)} results.")
        for r in res[:4]:
            print(f"  * {r['title']} -> {r['url']}")
    
    with open("bing_candidates.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    print("Done. Saved bing_candidates.json")
