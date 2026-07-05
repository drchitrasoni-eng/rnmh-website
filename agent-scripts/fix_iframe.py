import re

new_iframe_src = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.5888669566093!2d75.74740668399413!3d26.88480041649315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396db5509560e757%3A0xf39ab10b9bb91cff!2sR%20N%20Multispeciality%20hospital!5e0!3m2!1sen!2ssg!4v1781788811120!5m2!1sen!2ssg"

for filepath in ['site/location.html', 'site/hi/location.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We find the existing iframe and replace its src
    html = re.sub(r'src="https://www\.google\.com/maps/embed\?pb=[^"]+"', f'src="{new_iframe_src}"', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Map iframe updated.")
