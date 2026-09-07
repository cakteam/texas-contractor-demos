import subprocess

html_test = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div id="res"></div>
<script>
document.getElementById('res').innerText = 'innerWidth: ' + window.innerWidth + ', innerHeight: ' + window.innerHeight + ', clientWidth: ' + document.documentElement.clientWidth;
</script>
</body>
</html>
"""

with open("viewport_test.html", "w") as f:
    f.write(html_test)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=390,844",
    "--dump-dom",
    "viewport_test.html"
]
proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(proc.stdout)
