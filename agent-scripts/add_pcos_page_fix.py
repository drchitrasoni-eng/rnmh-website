import os
import re
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

def create_page(slug, service, location, is_hi=False):
    # Base on an existing gynaecology page
    source = f"site/hi/treatments/pregnancy-care-hospital-jaipur.html" if is_hi else f"site/treatments/pregnancy-care-hospital-jaipur.html"
    target = f"site/hi/treatments/{slug}.html" if is_hi else f"site/treatments/{slug}.html"
    
    with open(source, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the H1 and Title
    old_h1_en = "Pregnancy Care Hospital in Jaipur"
    old_h1_hi = "जयपुर में प्रेगनेंसी केयर हॉस्पिटल"
    
    new_h1 = f"{service} in {location}" if not is_hi else f"निर्माण नगर, जयपुर में {service}"
    
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{new_h1}</h1>', html)
    html = re.sub(r'<title>.*?</title>', f'<title>{new_h1} | R N Multispeciality Hospital</title>', html)
    
    # Replace lead text
    lead_en = "Consultation for PCOS, irregular periods and women’s health concerns at RNMH, Nirman Nagar."
    lead_hi = "PCOS, अनियमित पीरियड्स और महिला स्वास्थ्य समस्याओं के लिए कंसल्टेशन, RNMH निर्माण नगर में।"
    
    lead_text = lead_hi if is_hi else lead_en
    html = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{lead_text}</p>', html, count=1)
    
    # Also fix breadcrumbs for English if needed, but it's fine.
    
    with open(target, 'w', encoding='utf-8') as f:
        f.write(html)
        
create_page("pcos-treatment-jaipur", "PCOS & Period Problems Treatment", "Jaipur", is_hi=False)
create_page("pcos-treatment-jaipur", "PCOS एवं पीरियड्स का इलाज", "Jaipur", is_hi=True)

# Append to sitemap
with open("site/sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = sitemap.replace("</urlset>", "")
sitemap += f"""  <url>
    <loc>https://rnmh.in/treatments/pcos-treatment-jaipur.html</loc>
    <lastmod>{today}</lastmod>
  </url>
  <url>
    <loc>https://rnmh.in/hi/treatments/pcos-treatment-jaipur.html</loc>
    <lastmod>{today}</lastmod>
  </url>
</urlset>"""

with open("site/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
    
print("Added PCOS page successfully.")
