import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the script block
    script_pattern = re.compile(r'(<script>\s*\(function\(\)\{\s*try \{\s*var params = new URLSearchParams.*?\}\)\(\);\s*</script>)', re.DOTALL)
    
    # Find the link blocks
    link_pattern = re.compile(r'(<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*<link href="https://fonts\.googleapis\.com/css2[^"]+" rel="stylesheet">\s*<link rel="stylesheet" href="[^"]+">)', re.DOTALL)
    
    # Check if they are in the wrong order
    script_match = script_pattern.search(content)
    link_match = link_pattern.search(content)
    
    if script_match and link_match:
        # If script comes before links
        if script_match.start() < link_match.start():
            script_text = script_match.group(1)
            link_text = link_match.group(1)
            
            # replace the original script text with nothing, and the link text with link + script
            content = content.replace(link_text, link_text + '\n' + script_text)
            content = content.replace(script_text + '\n', '', 1) # only replace the first occurrence (the original)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    return False

changed = 0
for root, dirs, files in os.walk('site'):
    for file in files:
        if file.endswith('.html'):
            if process_file(os.path.join(root, file)):
                changed += 1

print(f"Fixed {changed} files")
