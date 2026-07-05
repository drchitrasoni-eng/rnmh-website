import re
import os

def fix_html(filepath, is_hi=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove locality block completely
    locality_pattern = re.compile(r'<!-- LOCALITY BLOCK -->\s*<section id="locality">.*?</section>\s*', re.DOTALL)
    html = locality_pattern.sub('', html)

    # 2. Fix grid-3 for Specialities and Doctors
    # In index.html, Specialities starts with <!-- SPECIALITIES --> and has <div style="max-width:800px; margin: 32px auto 0;">
    spec_pattern = re.compile(r'(<!-- SPECIALITIES -->\s*<section id="specialities"><div class="wrap">\s*<div class="sec-head">.*?</div>)\s*<div style="max-width:800px; margin: 32px auto 0;">', re.DOTALL)
    html = spec_pattern.sub(r'\1\n  <div class="grid-3" style="margin-top:32px;">', html)

    # Doctors starts with <!-- FEATURED DOCTORS -->
    doc_pattern = re.compile(r'(<!-- FEATURED DOCTORS -->\s*<section style="background:var\(--teal-soft\)\"><div class="wrap">\s*<div class="sec-head">.*?</div>)\s*<div style="max-width:800px; margin: 32px auto 0;">', re.DOTALL)
    html = doc_pattern.sub(r'\1\n  <div class="grid-3" style="margin-top:32px;">', html)

    # 3. Clean up Hero Section
    if not is_hi:
        hero_pattern = re.compile(r'(<!-- HERO: answer-first for GEO -->\s*<section class="hero"><div class="wrap">\s*<div>\s*<span class="eyebrow">.*?</span>\s*<h1>).*?(</h1>\s*<p class="lead">).*?(</p>)\s*<p class="hero-locality-support".*?</p>\s*<p class="hero-specialties-text".*?</p>', re.DOTALL)
        
        replacement = r'\1Trusted multispeciality care in Nirman Nagar, Jaipur\2R N Multispeciality Hospital is a 50-bed multispeciality hospital at 109-110, Shiv Shakti Nagar, Nirman Nagar, Jaipur. We provide 24x7 emergency care, specialist consultations, surgical services, diagnostics and cashless insurance support under one roof.\3'
        html = hero_pattern.sub(replacement, html)
    else:
        # Hindi Hero
        hero_pattern = re.compile(r'(<!-- HERO: answer-first for GEO -->\s*<section class="hero"><div class="wrap">\s*<div>\s*<span class="eyebrow">.*?</span>\s*<h1>).*?(</h1>\s*<p class="lead">).*?(</p>)\s*<p class="hero-locality-support".*?</p>\s*<p class="hero-specialties-text".*?</p>', re.DOTALL)
        
        replacement = r'\1निर्माण नगर, जयपुर में विश्वसनीय मल्टीस्पेशलिटी केयर\2R N Multispeciality Hospital निर्माण नगर, जयपुर में एक 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है। हम 24x7 इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, सर्जरी, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता एक ही छत के नीचे प्रदान करते हैं।\3'
        html = hero_pattern.sub(replacement, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html('site/index.html', is_hi=False)
fix_html('site/hi/index.html', is_hi=True)
print("Fixed layout grids, removed locality block, and cleaned up hero.")
