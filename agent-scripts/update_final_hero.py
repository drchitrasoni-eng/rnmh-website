import re

def update_english():
    with open('site/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The current hero in English:
    # <span class="eyebrow">50-Bed Multispeciality Hospital near Mansarovar Metro Station</span>
    # <h1>Trusted multispeciality care in Nirman Nagar, Jaipur</h1>
    # <p class="lead">R N Multispeciality Hospital is a 50-bed multispeciality hospital at 109-110, Shiv Shakti Nagar, Nirman Nagar, Jaipur. We provide 24x7 emergency care, specialist consultations, surgical services, diagnostics and cashless insurance support under one roof.</p>
    
    new_hero = """<span class="eyebrow">50-Bed Multispeciality Hospital in Nirman Nagar, Jaipur</span>
    <h1>Trusted multispeciality care in Jaipur, available 24x7</h1>
    <p class="lead">R N Multispeciality Hospital is a 50-bed hospital near Mansarovar Metro Station, offering emergency care, specialist consultations, surgical services, diagnostics, and cashless insurance support under one roof.</p>
    <p class="hero-specialties-text" style="color: var(--muted); font-size: 0.95rem; font-weight: 500; margin-bottom: 24px; line-height: 1.6;">General &amp; Laparoscopic Surgery &middot; Obstetrics &amp; Gynaecology &middot; Pain Management &amp; Spine Care &middot; Orthopaedics &middot; Urology &middot; Neurosurgery &middot; ENT &middot; General Medicine &middot; Pathology</p>"""

    pattern = re.compile(r'<span class="eyebrow">.*?</span>\s*<h1>.*?</h1>\s*<p class="lead">.*?</p>', re.DOTALL)
    
    # Check if we already have hero-specialties-text and remove it if so
    html = re.sub(r'<p class="hero-specialties-text".*?</p>\s*', '', html, flags=re.DOTALL)
    
    html = pattern.sub(new_hero, html)
    
    with open('site/index.html', 'w', encoding='utf-8') as f:
        f.write(html)


def update_hindi():
    with open('site/hi/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_hero = """<span class="eyebrow">निर्माण नगर, जयपुर में 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</span>
    <h1>जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर, 24x7 उपलब्ध</h1>
    <p class="lead">R N Multispeciality Hospital मानसरोवर मेट्रो स्टेशन के पास एक 50-बेड हॉस्पिटल है, जो एक ही छत के नीचे इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, सर्जिकल सेवाएँ, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता प्रदान करता है।</p>
    <p class="hero-specialties-text" style="color: var(--muted); font-size: 0.95rem; font-weight: 500; margin-bottom: 24px; line-height: 1.6;">जनरल व लैप्रोस्कोपिक सर्जरी &middot; स्त्री एवं प्रसूति रोग &middot; पेन मैनेजमेंट व स्पाइन केयर &middot; हड्डी रोग &middot; यूरोलॉजी &middot; न्यूरोसर्जरी &middot; ईएनटी &middot; जनरल मेडिसिन &middot; पैथोलॉजी</p>"""

    pattern = re.compile(r'<span class="eyebrow">.*?</span>\s*<h1>.*?</h1>\s*<p class="lead">.*?</p>', re.DOTALL)
    
    html = re.sub(r'<p class="hero-specialties-text".*?</p>\s*', '', html, flags=re.DOTALL)
    html = pattern.sub(new_hero, html)
    
    with open('site/hi/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_english()
update_hindi()
print("Hero sections updated successfully.")
