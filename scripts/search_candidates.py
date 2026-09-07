import urllib.request
import urllib.parse
import re
import json
import html

queries = [
    'roofing contractor Fort Worth TX site:*.com -yelp -angi -bbb -thumbtack',
    'HVAC repair Plano TX site:*.com -yelp -angi -bbb -thumbtack',
    'garage door repair Arlington TX site:*.com -yelp -angi -bbb -thumbtack',
    'foundation repair Dallas TX site:*.com -yelp -angi -bbb -thumbtack',
    'emergency plumbing Irving TX site:*.com -yelp -angi -bbb -thumbtack',
    'tree service Fort Worth TX site:*.com -yelp -angi -bbb -thumbtack',
    'water damage restoration Dallas TX site:*.com -yelp -angi -bbb -thumbtack',
]

def search_duckduckgo(query, max_results=10):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    results = []
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            content = response.read().decode("utf-8", errors="ignore")
            blocks = re.findall(r'<div class="result__body">([\s\S]*?)</div>\s*</div>', content)
            for b in blocks:
                title_match = re.search(r'<a class="result__url"[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>', b)
                snippet_match = re.search(r'<a class="result__snippet[^>]*>([\s\S]*?)</a>', b)
                title_text_match = re.search(r'<h2 class="result__title">[\s\S]*?<a[^>]*>([\s\S]*?)</a>', b)
                
                title = re.sub(r'<[^>]+>', '', title_text_match.group(1)).strip() if title_text_match else ""
                snippet = re.sub(r'<[^>]+>', '', snippet_match.group(1)).strip() if snippet_match else ""
                raw_url = title_match.group(1).strip() if title_match else ""
                
                actual_url = raw_url
                if "uddg=" in raw_url:
                    m = re.search(r'uddg=([^&]+)', raw_url)
                    if m:
                        actual_url = urllib.parse.unquote(m.group(1))
                
                if actual_url and actual_url.startswith("http"):
                    results.append({
                        "title": html.unescape(title),
                        "snippet": html.unescape(snippet),
                        "url": actual_url
                    })
                if len(results) >= max_results:
                    break
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return results

if __name__ == "__main__":
    all_results = {}
    for q in queries:
        print(f"Searching: {q}")
        res = search_duckduckgo(q, max_results=8)
        all_results[q] = res
        print(f"Found {len(res)} results.")
    
    with open("raw_search_results.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("Saved raw_search_results.json")
