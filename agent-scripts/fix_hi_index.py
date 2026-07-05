import re

with open('site/hi/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all <div style="max-width:800px; margin: 32px auto 0;"> EXCEPT the one under FAQ
# The FAQ one is preceded by "अक्सर पूछे जाने वाले सवाल"

# Let's just find and replace them manually using split or regex
parts = html.split('<div style="max-width:800px; margin: 32px auto 0;">')

if len(parts) == 6: # 1 before first, between 1&2, 2&3, 3&4, 4&5, 5&6. So 5 matches.
    # index 1, 2, 4 are the ones we want to replace with grid-3
    # Wait, the 3rd one might be FAQ?
    # Let's check the text right before each split.
    new_html = parts[0]
    for i in range(1, len(parts)):
        # What is the content right before the split?
        prev_chunk = parts[i-1]
        if "अक्सर पूछे जाने वाले सवाल" in prev_chunk[-200:]:
            new_html += '<div style="max-width:800px; margin: 32px auto 0;">' + parts[i]
        else:
            new_html += '<div class="grid-3" style="margin-top:32px;">' + parts[i]
            
    with open('site/hi/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
else:
    print("Failed to split properly: ", len(parts))

