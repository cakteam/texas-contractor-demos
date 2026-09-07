import subprocess
import os
import json
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We can run chrome with --dump-dom, but better: run a node script using puppeteer or a python script that evaluates JS
# Wait, let's see what npm packages or node scripts we can use. Node is v22.22.3!
# Can we use Chrome DevTools Protocol or fetch via node or evaluate?
# Actually, we can inject a script right into index.html that writes overflowing elements to a div or console!
