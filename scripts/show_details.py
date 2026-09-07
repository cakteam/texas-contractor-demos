import json

d = json.load(open('top3_scraped_details.json', encoding='utf-8'))
for k in d:
    with open(f"{k}_content.txt", "w", encoding="utf-8") as out:
        out.write(f"=== {k.upper()} ===\n")
        out.write("URL: " + d[k]['url'] + "\n\n")
        out.write("--- TEXT LINES ---\n")
        for line in d[k]['text_lines']:
            out.write(line + "\n")
        out.write("\n--- IMAGES ---\n")
        for img in d[k]['images']:
            out.write(img + "\n")
print("Exported details to text files.")
