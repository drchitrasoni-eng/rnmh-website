import os
import re
from PIL import Image

# 1. Resize and convert logo.png -> logo.webp
logo_path = 'site/assets/img/logo.png'
logo_webp = 'site/assets/img/logo.webp'
if os.path.exists(logo_path):
    with Image.open(logo_path) as img:
        img.thumbnail((100, 100), Image.Resampling.LANCZOS)
        img.save(logo_webp, 'WEBP', quality=85)

# 2. Resize exterior.webp for mobile
ext_path = 'site/assets/img/exterior.webp'
ext_mobile = 'site/assets/img/exterior-mobile.webp'
if os.path.exists(ext_path):
    with Image.open(ext_path) as img:
        img.thumbnail((800, 800), Image.Resampling.LANCZOS)
        img.save(ext_mobile, 'WEBP', quality=80)

# Read CSS content for inlining
css_path = 'site/assets/css/style.css'
css_content = ''
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()

# 3. Process HTML files
gtm_original_pattern = re.compile(
    r'<script>\(function\(w,d,s,l,i\)\{.*?\}\)\(window,document,\'script\',\'dataLayer\',\'GTM-KNW5HMMZ\'\);</script>',
    re.DOTALL
)

css_link_pattern = re.compile(r'<link rel="stylesheet" href="[^"]*style\.css\?[^"]*">', re.DOTALL)
css_link_pattern_fallback = re.compile(r'<link rel="stylesheet" href="[^"]*style\.css">', re.DOTALL)

changed_files = 0
for root, _, files in os.walk('site'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            # Inline CSS
            if '<style id="critical-css">' not in new_content:
                if css_link_pattern.search(new_content) or css_link_pattern_fallback.search(new_content):
                    style_tag = f'<style id="critical-css">\n{css_content}\n</style>'
                    new_content = css_link_pattern.sub(style_tag, new_content)
                    new_content = css_link_pattern_fallback.sub(style_tag, new_content)
            
            # Delay GTM
            match = gtm_original_pattern.search(new_content)
            if match and 'setTimeout' not in match.group(0):
                # We extract the inner function call and wrap it in setTimeout
                inner = match.group(0).replace('<script>', '').replace('</script>', '')
                wrapped = f'<script>\nsetTimeout(function(){{\n{inner}\n}}, 500);\n</script>'
                new_content = new_content.replace(match.group(0), wrapped)
            
            # Change logo.png to logo.webp
            new_content = new_content.replace('src="assets/img/logo.png"', 'src="assets/img/logo.webp"')
            new_content = new_content.replace('src="../assets/img/logo.png"', 'src="../assets/img/logo.webp"')
            
            # Add srcset to exterior image
            # Find the hero image tag and add srcset
            # <img src="assets/img/exterior.webp" fetchpriority="high" alt="...">
            ext_img = '<img src="assets/img/exterior.webp"'
            if ext_img in new_content and 'srcset=' not in new_content:
                new_content = new_content.replace(
                    ext_img, 
                    '<img src="assets/img/exterior.webp" srcset="assets/img/exterior-mobile.webp 800w, assets/img/exterior.webp 1216w" sizes="(max-width: 800px) 100vw, 1216px"'
                )
            
            ext_img_rel = '<img src="../assets/img/exterior.webp"'
            if ext_img_rel in new_content and 'srcset=' not in new_content:
                new_content = new_content.replace(
                    ext_img_rel, 
                    '<img src="../assets/img/exterior.webp" srcset="../assets/img/exterior-mobile.webp 800w, ../assets/img/exterior.webp 1216w" sizes="(max-width: 800px) 100vw, 1216px"'
                )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed_files += 1

print(f"Processed images and updated {changed_files} HTML files.")
