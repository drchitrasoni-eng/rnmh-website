import os
import re

def update_html():
    for root, dirs, files in os.walk('site'):
        if "node_modules" in root:
            continue
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            modified = False

            # Wrap display phone numbers
            if '0141 239 0320' in content:
                # We need to be careful not to wrap it multiple times
                content = re.sub(r'(?<!<span class="js-phone-display">)0141 239 0320', '<span class="js-phone-display">0141 239 0320</span>', content)
                modified = True
                
            # Add class to tel links
            if 'href="tel:+911412390320"' in content:
                content = re.sub(r'href="tel:\+911412390320"(?! class="js-phone-link")', 'href="tel:+911412390320" class="js-phone-link"', content)
                modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    update_html()
    print("HTML updated for phone classes")
