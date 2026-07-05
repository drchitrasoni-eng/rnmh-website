import os
import re

changed_files = 0
for root, dirs, files in os.walk('site'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            # Add lazy loading to doctor images
            new_content = re.sub(r'<img src="assets/img/docs/([^"]+)"', r'<img loading="lazy" src="assets/img/docs/\1"', new_content)
            new_content = re.sub(r'<img src="../assets/img/docs/([^"]+)"', r'<img loading="lazy" src="../assets/img/docs/\1"', new_content)
            
            # Remove duplicate loading="lazy" if it happens
            new_content = new_content.replace('loading="lazy" loading="lazy"', 'loading="lazy"')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed_files += 1

print(f"Added loading='lazy' to doctor images in {changed_files} files.")
