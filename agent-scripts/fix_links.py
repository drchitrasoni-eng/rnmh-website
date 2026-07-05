import os
import re

def fix_all_html():
    for root, dirs, files in os.walk('site'):
        if "node_modules" in root:
            continue
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)
            filepath_fwd = filepath.replace('\\', '/')
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            modified = False

            is_hi = '/hi/' in filepath_fwd
            
            # Calculate depth correctly based on path relative to 'site/'
            rel_path = filepath_fwd.split('site/')[1]
            depth = rel_path.count('/')
            
            # base_dir always goes back to 'site/'
            base_dir = '../' * depth
            
            if is_hi:
                # Inside 'hi/', the link should go to 'site/hi/...'
                hi_base = base_dir + 'hi/'
                
                # However, if we are linking from hi/index.html to hi/doctors.html,
                # hi_base is '../hi/'. So '../hi/doctors.html' works perfectly.
                # English equivalent link
                en_equivalent = rel_path.replace('hi/', '', 1)
                en_link = base_dir + en_equivalent
                if en_equivalent == '':
                    en_link = base_dir + 'index.html'

                nav_menu = f'<nav class="menu"><a href="{hi_base}index.html">होम</a><a href="{hi_base}index.html#specialities">विभाग</a><a href="{hi_base}doctors.html">डॉक्टर</a><a href="{hi_base}index.html#facilities">सुविधाएँ</a><a href="{hi_base}index.html#reviews">समीक्षाएँ</a><a href="{hi_base}contact.html">संपर्क</a><a class="lang" href="{en_link}">English</a><a class="btn btn-primary js-wa" href="#">अपॉइंटमेंट बुक करें</a></nav>'
            else:
                # English page
                hi_equivalent = 'hi/' + rel_path
                hi_link = base_dir + hi_equivalent

                nav_menu = f'<nav class="menu"><a href="{base_dir}index.html">Home</a><a href="{base_dir}index.html#specialities">Specialities</a><a href="{base_dir}doctors.html">Doctors</a><a href="{base_dir}index.html#facilities">Facilities</a><a href="{base_dir}index.html#reviews">Reviews</a><a href="{base_dir}contact.html">Contact</a><a class="lang" href="{hi_link}">हिन्दी</a><a class="btn btn-primary js-wa" href="#">Book appointment</a></nav>'

            nav_match = re.search(r'<nav class="menu">.*?</nav>', content, flags=re.DOTALL)
            if nav_match:
                if nav_match.group(0) != nav_menu:
                    content = content[:nav_match.start()] + nav_menu + content[nav_match.end():]
                    modified = True

            # Also fix the mobile menu links
            if is_hi:
                mob_menu = f'<div class="mobile-menu" id="mobileMenu"><a href="{hi_base}index.html">होम</a><a href="{hi_base}doctors.html">डॉक्टर</a><a href="{hi_base}contact.html">संपर्क</a><a href="{en_link}">English</a><a class="btn btn-primary js-wa" href="#">अपॉइंटमेंट बुक करें</a></div>'
            else:
                mob_menu = f'<div class="mobile-menu" id="mobileMenu"><a href="{base_dir}index.html">Home</a><a href="{base_dir}doctors.html">Doctors</a><a href="{base_dir}contact.html">Contact</a><a href="{hi_link}">हिन्दी</a><a class="btn btn-primary js-wa" href="#">Book appointment</a></div>'

            mob_match = re.search(r'<div class="mobile-menu".*?</div>', content, flags=re.DOTALL)
            if mob_match:
                if mob_match.group(0) != mob_menu:
                    content = content[:mob_match.start()] + mob_menu + content[mob_match.end():]
                    modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    fix_all_html()
    print("Nav links fixed")
