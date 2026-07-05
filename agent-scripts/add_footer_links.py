import os
import re

links_en = [
    '<a href="{prefix}treatments/gynaecologist-near-nirman-nagar-jaipur.html">Gynaecologist near Nirman Nagar</a>',
    '<a href="{prefix}treatments/gynaecologist-near-mansarovar-metro-station.html">Gynaecologist near Mansarovar Metro</a>',
    '<a href="{prefix}treatments/pregnancy-care-hospital-near-mansarovar-metro.html">Pregnancy care near Mansarovar Metro</a>',
    '<a href="{prefix}treatments/fertility-doctor-nirman-nagar-jaipur.html">Fertility Doctor Nirman Nagar</a>',
    '<a href="{prefix}treatments/obgyn-kings-road-jaipur.html">OB-GYN Kings Road Jaipur</a>',
    '<a href="{prefix}treatments/hospital-near-mansarovar-metro-station.html">Hospital near Mansarovar Metro</a>',
    '<a href="{prefix}treatments/multispeciality-hospital-kings-road-jaipur.html">Multispeciality Hospital Kings Road</a>',
    '<a href="{prefix}treatments/24x7-emergency-hospital-nirman-nagar-jaipur.html">24x7 Emergency Hospital in Nirman Nagar</a>',
    '<a href="{prefix}treatments/cashless-hospital-near-mansarovar-jaipur.html">Cashless Hospital near Mansarovar</a>',
    '<a href="{prefix}treatments/laparoscopic-surgeon-near-mansarovar-metro.html">Laparoscopic Surgeon near Mansarovar Metro</a>',
    '<a href="{prefix}treatments/general-surgeon-nirman-nagar-jaipur.html">General Surgeon Nirman Nagar</a>',
    '<a href="{prefix}treatments/laser-piles-treatment-kings-road-jaipur.html">Laser Piles Treatment Kings Road</a>',
    '<a href="{prefix}treatments/hernia-surgery-nirman-nagar-jaipur.html">Hernia Surgery Nirman Nagar</a>',
    '<a href="{prefix}treatments/back-pain-treatment-nirman-nagar-jaipur.html">Back Pain Treatment Nirman Nagar</a>',
    '<a href="{prefix}treatments/spine-specialist-near-mansarovar-metro.html">Spine Specialist near Mansarovar Metro</a>',
    '<a href="{prefix}treatments/pain-management-doctor-kings-road-jaipur.html">Pain Management Kings Road</a>'
]

links_hi = [
    '<a href="{prefix}hi/treatments/gynaecologist-near-nirman-nagar-jaipur.html">निर्माण नगर के पास गायनेकोलॉजिस्ट</a>',
    '<a href="{prefix}hi/treatments/gynaecologist-near-mansarovar-metro-station.html">मानसरोवर मेट्रो के पास गायनेकोलॉजिस्ट</a>',
    '<a href="{prefix}hi/treatments/pregnancy-care-hospital-near-mansarovar-metro.html">मानसरोवर मेट्रो के पास प्रेगनेंसी केयर</a>',
    '<a href="{prefix}hi/treatments/fertility-doctor-nirman-nagar-jaipur.html">निर्माण नगर जयपुर फर्टिलिटी डॉक्टर</a>',
    '<a href="{prefix}hi/treatments/obgyn-kings-road-jaipur.html">किंग्स रोड जयपुर OB-GYN</a>',
    '<a href="{prefix}hi/treatments/hospital-near-mansarovar-metro-station.html">मानसरोवर मेट्रो के पास हॉस्पिटल</a>',
    '<a href="{prefix}hi/treatments/multispeciality-hospital-kings-road-jaipur.html">किंग्स रोड जयपुर मल्टीस्पेशलिटी हॉस्पिटल</a>',
    '<a href="{prefix}hi/treatments/24x7-emergency-hospital-nirman-nagar-jaipur.html">निर्माण नगर 24x7 इमरजेंसी हॉस्पिटल</a>',
    '<a href="{prefix}hi/treatments/cashless-hospital-near-mansarovar-jaipur.html">मानसरोवर के पास कैशलेस हॉस्पिटल</a>',
    '<a href="{prefix}hi/treatments/laparoscopic-surgeon-near-mansarovar-metro.html">मानसरोवर मेट्रो लेप्रोस्कोपिक सर्जन</a>',
    '<a href="{prefix}hi/treatments/general-surgeon-nirman-nagar-jaipur.html">निर्माण नगर जनरल सर्जन</a>',
    '<a href="{prefix}hi/treatments/laser-piles-treatment-kings-road-jaipur.html">किंग्स रोड लेजर पाइल्स ट्रीटमेंट</a>',
    '<a href="{prefix}hi/treatments/hernia-surgery-nirman-nagar-jaipur.html">निर्माण नगर हर्निया सर्जरी</a>',
    '<a href="{prefix}hi/treatments/back-pain-treatment-nirman-nagar-jaipur.html">निर्माण नगर बैक पेन ट्रीटमेंट</a>',
    '<a href="{prefix}hi/treatments/spine-specialist-near-mansarovar-metro.html">मानसरोवर मेट्रो के पास स्पाइन स्पेशलिस्ट</a>',
    '<a href="{prefix}hi/treatments/pain-management-doctor-kings-road-jaipur.html">किंग्स रोड पेन मैनेजमेंट डॉक्टर</a>'
]

def process_html_files(base_dir):
    for root, _, files in os.walk(base_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                # Determine prefix for internal links
                depth = filepath.replace(base_dir, "").count(os.sep) - 1
                prefix = ""
                if depth == 1:
                    prefix = "../"
                elif depth == 2:
                    prefix = "../../"
                
                # Hindi flag
                is_hi = "/hi/" in filepath or filepath.endswith("/hi/index.html")
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Build block
                if is_hi:
                    links = " &middot; ".join([l.format(prefix=prefix.replace("../../hi/", "../../").replace("../hi/", "../") if "/hi/" in prefix else prefix) for l in links_hi])
                    # Fix: If we are already in hi directory, prefix shouldn't double hi
                    links = " &middot; ".join([l.format(prefix=prefix) for l in links_hi]).replace(f"{prefix}hi/treatments", f"{prefix}treatments")
                    
                    block = f"""  <div class="footer-seo-links" style="border-top: 1px solid rgba(255,255,255,0.1); margin-top:30px; padding-top:20px;">
    <h4 style="margin-bottom:8px; font-size:14px;">स्थानीय खोज:</h4>
    <p style="font-size: 13px; line-height:1.6; color: rgba(255,255,255,0.7);">{links}</p>
  </div>
"""
                else:
                    links = " &middot; ".join([l.format(prefix=prefix) for l in links_en])
                    block = f"""  <div class="footer-seo-links" style="border-top: 1px solid rgba(255,255,255,0.1); margin-top:30px; padding-top:20px;">
    <h4 style="margin-bottom:8px; font-size:14px;">Local Searches:</h4>
    <p style="font-size: 13px; line-height:1.6; color: rgba(255,255,255,0.7);">{links}</p>
  </div>
"""

                if 'class="footer-seo-links"' not in content:
                    content = content.replace('<div class="copy">', block + '  <div class="copy">')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)

process_html_files("site")
print("Footer SEO links added to all pages.")
