import os
import re

def update_ui():
    for root, dirs, files in os.walk('site'):
        if "node_modules" in root:
            continue
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)
            filepath_fwd = filepath.replace('\\', '/')
            is_hi = '/hi/' in filepath_fwd
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            modified = False

            # 1. Update the .doc cards to include a "Book appointment" button next to "View profile"
            # We look for <a class="btn btn-teal" href="...">View profile</a> (or Hindi equivalent)
            # and append a <a class="btn btn-primary js-wa" href="#">Book on WhatsApp</a>
            
            view_profile_en = r'<a class="btn btn-teal" href="([^"]+)">View profile</a>'
            view_profile_hi = r'<a class="btn btn-teal" href="([^"]+)">प्रोफ़ाइल देखें</a>'

            def replacer(match):
                href = match.group(1)
                text = match.group(0)
                # Avoid adding multiple times
                book_btn_en = f'<button class="btn btn-primary js-wa" style="margin-left:8px">Book appointment</button>'
                book_btn_hi = f'<button class="btn btn-primary js-wa" style="margin-left:8px">अपॉइंटमेंट बुक करें</button>'
                btn = book_btn_hi if is_hi else book_btn_en
                return text + btn

            # First check if not already added to avoid duplicates
            if 'class="btn btn-primary js-wa" style="margin-left:8px"' not in content:
                new_content = re.sub(view_profile_en, replacer, content)
                new_content = re.sub(view_profile_hi, replacer, new_content)
                if new_content != content:
                    content = new_content
                    modified = True

            # 2. Fix mobile menu missing items
            # The mobile menu structure should match desktop nav but stack vertically.
            # We'll just replace the whole `<div class="mobile-menu".*?</div>` block
            rel_path = filepath_fwd.split('site/')[1]
            depth = rel_path.count('/')
            base_dir = '../' * depth
            
            if is_hi:
                hi_base = base_dir + 'hi/'
                en_equivalent = rel_path.replace('hi/', '', 1)
                en_link = base_dir + en_equivalent
                if en_equivalent == '':
                    en_link = base_dir + 'index.html'

                mob_menu = f'<div class="mobile-menu" id="mobileMenu"><a href="{hi_base}index.html">होम</a><a href="{hi_base}index.html#specialities">विभाग</a><a href="{hi_base}doctors.html">डॉक्टर</a><a href="{hi_base}index.html#facilities">सुविधाएँ</a><a href="{hi_base}index.html#reviews">समीक्षाएँ</a><a href="{hi_base}contact.html">संपर्क</a><a href="{en_link}">English</a><a class="btn btn-primary js-wa" href="#" style="margin-top:8px; display:inline-block; text-align:center;">अपॉइंटमेंट बुक करें</a></div>'
            else:
                hi_equivalent = 'hi/' + rel_path
                hi_link = base_dir + hi_equivalent

                mob_menu = f'<div class="mobile-menu" id="mobileMenu"><a href="{base_dir}index.html">Home</a><a href="{base_dir}index.html#specialities">Specialities</a><a href="{base_dir}doctors.html">Doctors</a><a href="{base_dir}index.html#facilities">Facilities</a><a href="{base_dir}index.html#reviews">Reviews</a><a href="{base_dir}contact.html">Contact</a><a href="{hi_link}">हिन्दी</a><a class="btn btn-primary js-wa" href="#" style="margin-top:8px; display:inline-block; text-align:center;">Book appointment</a></div>'

            mob_match = re.search(r'<div class="mobile-menu".*?</div>', content, flags=re.DOTALL)
            if mob_match:
                if mob_match.group(0) != mob_menu:
                    content = content[:mob_match.start()] + mob_menu + content[mob_match.end():]
                    modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    # 3. Add CSS for .spec-banner optimization
    css_path = 'site/assets/css/style.css'
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        css_mod = False
        if '.spec-banner {' not in css and '.spec-banner{' not in css:
            css += '\n.spec-banner { max-height: 40vh; object-fit: cover; border-radius: 12px; width: 100%; display: block; }\n'
            css_mod = True
            
        # Add a flex wrapper to `.body` inside `.doc` if it doesn't already wrap buttons nicely
        # Actually, adding buttons side by side can wrap poorly if no flex. 
        # But we added `style="margin-left:8px"`. It should be fine.

        if css_mod:
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css)

if __name__ == '__main__':
    update_ui()
    print("UI tweaked")
