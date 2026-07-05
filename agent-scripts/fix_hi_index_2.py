import re

with open('site/hi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('<div style="max-width:800px; margin: 32px auto 0;">')
new_html = parts[0]
for i in range(1, len(parts)):
    prev_chunk = parts[i-1]
    if "अक्सर पूछे जाने वाले सवाल" in prev_chunk[-200:]:
        new_html += '<div style="max-width:800px; margin: 32px auto 0;">' + parts[i]
    else:
        new_html += '<div class="grid-3" style="margin-top:32px;">' + parts[i]
        
with open('site/hi/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Fixed hi grids.")
