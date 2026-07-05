import os
import re

def fix_alignment_and_video():
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

            # Fix YouTube iframe for local viewing
            if 'youtube-nocookie.com/embed/' in content:
                content = content.replace('youtube-nocookie.com/embed/', 'youtube.com/embed/')
                modified = True
            
            if 'referrerpolicy="strict-origin-when-cross-origin"' in content:
                content = content.replace('referrerpolicy="strict-origin-when-cross-origin"', '')
                modified = True

            # Fix button alignment (remove the margin-left:8px which causes the misalignment)
            if 'style="margin-left:8px">Book appointment</button>' in content:
                content = content.replace('style="margin-left:8px">Book appointment</button>', 'style="margin-top:2px; width: 100%; justify-content: center;">Book appointment</button>')
                modified = True
                
            if 'style="margin-left:8px">अपॉइंटमेंट बुक करें</button>' in content:
                content = content.replace('style="margin-left:8px">अपॉइंटमेंट बुक करें</button>', 'style="margin-top:2px; width: 100%; justify-content: center;">अपॉइंटमेंट बुक करें</button>')
                modified = True

            # Ensure the "View profile" button also stretches to full width
            # We can just add inline styles or do it via CSS
            # We'll do it via CSS, but let's make sure the inline style is applied just in case
            if '<a class="btn btn-teal" href="' in content and 'View profile' in content:
                content = re.sub(r'(<a class="btn btn-teal" href="[^"]+")(>View profile</a>)', r'\1 style="width: 100%; justify-content: center;"\2', content)
                modified = True

            if '<a class="btn btn-teal" href="' in content and 'प्रोफ़ाइल देखें' in content:
                content = re.sub(r'(<a class="btn btn-teal" href="[^"]+")(>प्रोफ़ाइल देखें</a>)', r'\1 style="width: 100%; justify-content: center;"\2', content)
                modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    # Add CSS for .doc .body .btn just to be safe
    css_path = 'site/assets/css/style.css'
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        css_mod = False
        if '.doc .body .btn { width: 100%; justify-content: center; }' not in css:
            css += '\n.doc .body .btn { width: 100%; justify-content: center; }\n'
            css_mod = True
            
        if css_mod:
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)

if __name__ == '__main__':
    fix_alignment_and_video()
    print("Alignment and videos fixed")
