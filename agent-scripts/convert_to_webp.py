import os
import re
from PIL import Image

def convert_to_webp(filepath):
    webp_path = os.path.splitext(filepath)[0] + '.webp'
    if os.path.exists(webp_path):
        return webp_path
    try:
        with Image.open(filepath) as img:
            img.save(webp_path, 'WEBP', quality=80)
        return webp_path
    except Exception as e:
        print(f"Failed to convert {filepath}: {e}")
        return None

# Find all images and convert
image_dir = 'site/assets/img'
image_map = {} # old_src -> new_src

for root, _, files in os.walk(image_dir):
    for f in files:
        if f.endswith('.jpg') or f.endswith('.png'):
            if f in ['logo.png', 'logo-full.png']:
                continue # skip logos just to be safe with transparency sometimes, though webp supports it
            filepath = os.path.join(root, f)
            webp_path = convert_to_webp(filepath)
            if webp_path:
                old_src = filepath.replace('site/', '')
                new_src = webp_path.replace('site/', '')
                image_map[old_src] = new_src
                # also map relative paths
                image_map['../' + old_src] = '../' + new_src

changed_files = 0
# Update HTML files
for root, _, files in os.walk('site'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # We only replace src inside <img> tags, not <meta> tags
            def repl(match):
                prefix = match.group(1)
                src = match.group(2)
                suffix = match.group(3)
                if src in image_map:
                    return f'{prefix}{image_map[src]}{suffix}'
                return match.group(0)
            
            new_content = re.sub(r'(<img[^>]*\s+src=")([^"]+)(")', repl, content)
            
            # Also update preload links
            new_content = re.sub(r'(<link[^>]*\s+href=")([^"]+)(")', repl, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed_files += 1

print(f"Converted images and updated {changed_files} HTML files.")
