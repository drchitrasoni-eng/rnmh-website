import os
import re

def update_english_homepage():
    filepath = "site/index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update Title and Meta Description
    html = re.sub(
        r'<title>.*?</title>',
        '<title>R N Multispeciality Hospital Jaipur | Kings Road, Nirman Nagar, Near Mansarovar Metro</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="R N Multispeciality Hospital is a 50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station. 24x7 emergency care, gynaecology, surgery, diagnostics, ICU/NICU and cashless insurance support.">',
        html
    )
    
    # 2. Update Hero Section
    html = html.replace(
        '<span class="eyebrow">50-Bed Multispeciality Hospital in Nirman Nagar, Jaipur</span>',
        '<span class="eyebrow">50-Bed Multispeciality Hospital near Mansarovar Metro Station</span>'
    )
    html = html.replace(
        '<h1>Trusted multispeciality care in Jaipur, available <span class="accent">24x7</span></h1>',
        '<h1>Trusted multispeciality care on Kings Road, Nirman Nagar, Jaipur</h1>'
    )
    html = html.replace(
        '<p class="lead">R N Multispeciality Hospital is a 50-bed hospital near Mansarovar Metro Station, offering emergency care, specialist consultations, surgical services, diagnostics, and cashless insurance support under one roof.</p>',
        '<p class="lead">R N Multispeciality Hospital is a 50-bed multispeciality hospital at 109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station. We provide 24x7 emergency care, specialist consultations, surgical services, diagnostics and cashless insurance support under one roof.</p>\n    <p class="hero-locality-support" style="color: var(--muted); font-size: 1rem; font-weight: 500; margin-bottom: 24px; line-height: 1.6;">Serving patients from Nirman Nagar, Mansarovar, Kings Road, Shyam Nagar, Brijlalpura, Gopalpura Bypass and nearby Jaipur areas.</p>'
    )
    
    # 3. Add Locality Block after stats section
    locality_block = """
<!-- LOCALITY BLOCK -->
<section id="locality"><div class="wrap">
  <div class="sec-head"><h2>Hospital near Mansarovar Metro Station, Kings Road and Nirman Nagar</h2></div>
  <p class="lead">R N Multispeciality Hospital is located on Main Kings Road in Nirman Nagar, Jaipur, close to Mansarovar Metro Station. The hospital is easily accessible for families from Nirman Nagar, Mansarovar, Shyam Nagar, Brijlalpura, Rail Nagar, Gopalpura Bypass, New Aatish Market and nearby Jaipur localities.</p>
  <p class="lead">Patients searching for a multispeciality hospital, gynaecologist, general surgeon, pain and spine specialist, diagnostic centre or 24x7 emergency hospital near Mansarovar Metro Station can visit RNMH for specialist-led care under one roof.</p>
</div></section>
"""
    if '<!-- LOCALITY BLOCK -->' not in html:
        html = html.replace('<!-- SPECIALITIES -->', locality_block + '\n<!-- SPECIALITIES -->')

    # 4. Add FAQs to HTML
    faq_html = """
    <div class="card"><div class="card-core"><h3>Is R N Multispeciality Hospital near Mansarovar Metro Station?</h3><p class="desc" style="margin-top:10px;">Yes. R N Multispeciality Hospital is located on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Which hospital is available on Kings Road, Nirman Nagar, Jaipur?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital is a 50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur, offering 24x7 emergency care, specialist consultations, surgery, diagnostics, ICU/NICU and cashless insurance support.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is there a gynaecologist near Nirman Nagar or Mansarovar Metro Station at RNMH?</h3><p class="desc" style="margin-top:10px;">Yes. Obstetrics, gynaecology and fertility consultations are available at R N Multispeciality Hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station.</p></div></div>
    <div class="card"><div class="card-core"><h3>Is RNMH accessible from Mansarovar and Shyam Nagar?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH is located in Nirman Nagar near Mansarovar Metro Station and is accessible from Mansarovar, Shyam Nagar, Brijlalpura, Gopalpura Bypass, Kings Road and nearby Jaipur areas.</p></div></div>
    <div class="card"><div class="card-core"><h3>Does RNMH provide emergency care near Kings Road Jaipur?</h3><p class="desc" style="margin-top:10px;">Yes. RNMH provides 24x7 emergency care at its hospital on Main Kings Road, Nirman Nagar, Jaipur.</p></div></div>
"""
    if "Is R N Multispeciality Hospital near Mansarovar Metro Station?" not in html:
        html = html.replace('<!-- REVIEWS -->', '</div>\n  <div class="grid-3" style="margin-top:32px;">' + faq_html + '\n  </div></section>\n\n<!-- REVIEWS -->')
        # We need to remove the existing closing tags in the FAQ section before adding them, or just inject into the existing grid
        # Actually, let's inject into the existing grid-3 of FAQ section
        pass

    # Wait, the better way to add FAQs to HTML is:
    faq_grid_pattern = r'(<div class="grid-3" style="margin-top:32px;">)'
    if "Is R N Multispeciality Hospital near Mansarovar Metro Station?" not in html:
        html = re.sub(faq_grid_pattern, r'\1\n' + faq_html.replace('\\', '\\\\'), html, count=1)

    # 5. Schema update
    # Just replace the whole schema script block for hospital
    # Let's find the first <script type="application/ld+json">
    new_hospital_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Hospital", "MedicalOrganization", "LocalBusiness"],
  "@id": "https://rnmh.in/#hospital",
  "name": "R N Multispeciality Hospital",
  "alternateName": "RNMH",
  "url": "https://rnmh.in/",
  "logo": "https://rnmh.in/assets/img/logo.png",
  "image": "https://rnmh.in/assets/img/exterior.jpg",
  "description": "R N Multispeciality Hospital is a 50-bed multispeciality hospital at 109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station. The hospital provides 24x7 emergency care, specialist consultations, surgery, diagnostics, ICU/NICU and cashless insurance support.",
  "telephone": "+91-141-239-0320",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "109-110, Shiv Shakti Nagar, Main Kings Road, Nirman Nagar",
    "addressLocality": "Jaipur",
    "addressRegion": "Rajasthan",
    "postalCode": "302019",
    "addressCountry": "IN"
  },
  "areaServed": [
    "Nirman Nagar",
    "Kings Road",
    "Mansarovar Metro Station",
    "Mansarovar",
    "Shyam Nagar",
    "Brijlalpura",
    "Gopalpura Bypass",
    "New Aatish Market",
    "Jaipur"
  ],
  "availableService": [
    "24x7 emergency care",
    "Obstetrics and Gynaecology",
    "Fertility consultation",
    "General and Laparoscopic Surgery",
    "Pain Management and Spine Care",
    "Orthopaedics",
    "Urology",
    "Neurosurgery",
    "ENT",
    "General Medicine",
    "Pathology and Diagnostics",
    "Cashless insurance support"
  ],
  "medicalSpecialty": [
    "Obstetrics and Gynaecology",
    "General Surgery",
    "Laparoscopic Surgery",
    "Pain Management",
    "Spine Care",
    "Orthopaedics",
    "Urology",
    "Neurosurgery",
    "ENT",
    "General Medicine",
    "Pathology"
  ],
  "openingHours": "Mo-Su 00:00-23:59",
  "sameAs": [
    "https://www.google.com/maps?cid=YOUR_CID_HERE",
    "https://www.youtube.com/@dr_chitra_soni",
    "https://www.youtube.com/@naveensoni1638",
    "https://www.youtube.com/@drrobinbothra",
    "https://www.instagram.com/drchitra_simplygynec/",
    "https://www.instagram.com/spine_joint_and_back_pain_",
    "https://www.instagram.com/dr_robin_rn_hospital/"
  ]
}
</script>"""

    # We replace the first schema block
    html = re.sub(
        r'<script type="application/ld\+json">\s*{\s*"@context":"https://schema\.org",\s*"@type":\["Hospital".*?</script>',
        new_hospital_schema,
        html,
        flags=re.DOTALL
    )

    # 6. FAQ Schema Update
    new_faq_schema_items = """    {
      "@type": "Question",
      "name": "Is R N Multispeciality Hospital near Mansarovar Metro Station?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. R N Multispeciality Hospital is located on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station."
      }
    },
    {
      "@type": "Question",
      "name": "Which hospital is available on Kings Road, Nirman Nagar, Jaipur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "R N Multispeciality Hospital is a 50-bed multispeciality hospital on Main Kings Road, Nirman Nagar, Jaipur, offering 24x7 emergency care, specialist consultations, surgery, diagnostics, ICU/NICU and cashless insurance support."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a gynaecologist near Nirman Nagar or Mansarovar Metro Station at RNMH?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Obstetrics, gynaecology and fertility consultations are available at R N Multispeciality Hospital on Main Kings Road, Nirman Nagar, Jaipur, near Mansarovar Metro Station."
      }
    },
    {
      "@type": "Question",
      "name": "Is RNMH accessible from Mansarovar and Shyam Nagar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. RNMH is located in Nirman Nagar near Mansarovar Metro Station and is accessible from Mansarovar, Shyam Nagar, Brijlalpura, Gopalpura Bypass, Kings Road and nearby Jaipur areas."
      }
    },
    {
      "@type": "Question",
      "name": "Does RNMH provide emergency care near Kings Road Jaipur?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. RNMH provides 24x7 emergency care at its hospital on Main Kings Road, Nirman Nagar, Jaipur."
      }
    },"""
    
    if "Is R N Multispeciality Hospital near Mansarovar Metro Station?" not in html:
        html = html.replace('"mainEntity": [', '"mainEntity": [\n' + new_faq_schema_items)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

def update_hindi_homepage():
    filepath = "site/hi/index.html"
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Title and Meta
    html = re.sub(
        r'<title>.*?</title>',
        '<title>आर एन मल्टीस्पेशलिटी हॉस्पिटल जयपुर | किंग्स रोड, निर्माण नगर, मानसरोवर मेट्रो के पास</title>',
        html
    )
    html = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="आर एन मल्टीस्पेशलिटी हॉस्पिटल मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है, मानसरोवर मेट्रो स्टेशन के पास। 24x7 इमरजेंसी, गायनेकोलॉजी, सर्जरी, डायग्नोस्टिक्स, ICU/NICU और कैशलेस इंश्योरेंस सहायता उपलब्ध।">',
        html
    )

    # Hero Section Hindi replacements
    # Need to see exactly what is in hi/index.html
    html = re.sub(
        r'<span class="eyebrow">.*?</span>',
        '<span class="eyebrow">मानसरोवर मेट्रो स्टेशन के पास 50-बेड मल्टीस्पेशलिटी हॉस्पिटल</span>',
        html, count=1 # Only first eyebrow in hero
    )
    html = re.sub(
        r'<h1>.*?</h1>',
        '<h1>किंग्स रोड, निर्माण नगर, जयपुर में भरोसेमंद मल्टीस्पेशलिटी केयर</h1>',
        html, count=1
    )
    html = re.sub(
        r'<p class="lead">.*?</p>',
        '<p class="lead">आर एन मल्टीस्पेशलिटी हॉस्पिटल 109-110, शिव शक्ति नगर, मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है, मानसरोवर मेट्रो स्टेशन के पास। यहाँ 24x7 इमरजेंसी केयर, विशेषज्ञ डॉक्टरों की सलाह, सर्जिकल सेवाएँ, डायग्नोस्टिक्स और कैशलेस इंश्योरेंस सहायता एक ही जगह उपलब्ध है。</p>\n    <p class="hero-locality-support" style="color: var(--muted); font-size: 1rem; font-weight: 500; margin-bottom: 24px; line-height: 1.6;">निर्माण नगर, मानसरोवर, किंग्स रोड, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास और आसपास के जयपुर क्षेत्रों के मरीजों के लिए सुविधाजनक स्थान।</p>',
        html, count=1
    )

    # Add Hindi locality block
    hindi_locality = """
<!-- LOCALITY BLOCK -->
<section id="locality"><div class="wrap">
  <div class="sec-head"><h2>मानसरोवर मेट्रो स्टेशन, किंग्स रोड और निर्माण नगर के पास हॉस्पिटल</h2></div>
  <p class="lead">आर एन मल्टीस्पेशलिटी हॉस्पिटल मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास। यह हॉस्पिटल निर्माण नगर, मानसरोवर, श्याम नगर, बृजलालपुरा, रेल नगर, गोपालपुरा बाइपास, न्यू आतिश मार्केट और आसपास के जयपुर क्षेत्रों के परिवारों के लिए आसानी से पहुँचने योग्य है।</p>
  <p class="lead">मानसरोवर मेट्रो स्टेशन के पास मल्टीस्पेशलिटी हॉस्पिटल, गायनेकोलॉजिस्ट, जनरल सर्जन, पेन व स्पाइन स्पेशलिस्ट, डायग्नोस्टिक सेंटर या 24x7 इमरजेंसी हॉस्पिटल खोज रहे मरीज RNMH में एक ही जगह विशेषज्ञों की देखरेख में इलाज के लिए आ सकते हैं।</p>
</div></section>
"""
    if '<!-- LOCALITY BLOCK -->' not in html:
        html = html.replace('<!-- SPECIALITIES -->', hindi_locality + '\n<!-- SPECIALITIES -->')

    # Add Hindi FAQs
    hindi_faqs = """
    <div class="card"><div class="card-core"><h3>क्या R N Multispeciality Hospital मानसरोवर मेट्रो स्टेशन के पास है?</h3><p class="desc" style="margin-top:10px;">हाँ। R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।</p></div></div>
    <div class="card"><div class="card-core"><h3>किंग्स रोड, निर्माण नगर, जयपुर में कौन सा हॉस्पिटल उपलब्ध है?</h3><p class="desc" style="margin-top:10px;">R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है, जहाँ 24x7 इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, सर्जरी, डायग्नोस्टिक्स, ICU/NICU और कैशलेस इंश्योरेंस सहायता उपलब्ध है।</p></div></div>
    <div class="card"><div class="card-core"><h3>क्या RNMH में निर्माण नगर या मानसरोवर मेट्रो स्टेशन के पास गायनेकोलॉजिस्ट उपलब्ध है?</h3><p class="desc" style="margin-top:10px;">हाँ। R N Multispeciality Hospital में ऑब्स्टेट्रिक्स, गायनेकोलॉजी और फर्टिलिटी कंसल्टेशन उपलब्ध है। हॉस्पिटल मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।</p></div></div>
    <div class="card"><div class="card-core"><h3>क्या RNMH मानसरोवर और श्याम नगर से आसानी से पहुँचा जा सकता है?</h3><p class="desc" style="margin-top:10px;">हाँ। RNMH निर्माण नगर में मानसरोवर मेट्रो स्टेशन के पास स्थित है और मानसरोवर, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास, किंग्स रोड और आसपास के जयपुर क्षेत्रों से आसानी से पहुँचा जा सकता है।</p></div></div>
    <div class="card"><div class="card-core"><h3>क्या RNMH किंग्स रोड जयपुर के पास इमरजेंसी केयर देता है?</h3><p class="desc" style="margin-top:10px;">हाँ। RNMH मेन किंग्स रोड, निर्माण नगर, जयपुर में 24x7 इमरजेंसी केयर उपलब्ध कराता है।</p></div></div>
"""
    faq_grid_pattern = r'(<div class="grid-3" style="margin-top:32px;">)'
    if "क्या R N Multispeciality Hospital मानसरोवर" not in html:
        html = re.sub(faq_grid_pattern, r'\1\n' + hindi_faqs.replace('\\', '\\\\'), html, count=1)

    hindi_faq_schema_items = """    {
      "@type": "Question",
      "name": "क्या R N Multispeciality Hospital मानसरोवर मेट्रो स्टेशन के पास है?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "हाँ। R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।"
      }
    },
    {
      "@type": "Question",
      "name": "किंग्स रोड, निर्माण नगर, जयपुर में कौन सा हॉस्पिटल उपलब्ध है?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "R N Multispeciality Hospital मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित 50-बेड मल्टीस्पेशलिटी हॉस्पिटल है, जहाँ 24x7 इमरजेंसी केयर, विशेषज्ञ कंसल्टेशन, सर्जरी, डायग्नोस्टिक्स, ICU/NICU और कैशलेस इंश्योरेंस सहायता उपलब्ध है।"
      }
    },
    {
      "@type": "Question",
      "name": "क्या RNMH में निर्माण नगर या मानसरोवर मेट्रो स्टेशन के पास गायनेकोलॉजिस्ट उपलब्ध है?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "हाँ। R N Multispeciality Hospital में ऑब्स्टेट्रिक्स, गायनेकोलॉजी और फर्टिलिटी कंसल्टेशन उपलब्ध है। हॉस्पिटल मेन किंग्स रोड, निर्माण नगर, जयपुर में स्थित है, मानसरोवर मेट्रो स्टेशन के पास।"
      }
    },
    {
      "@type": "Question",
      "name": "क्या RNMH मानसरोवर और श्याम नगर से आसानी से पहुँचा जा सकता है?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "हाँ। RNMH निर्माण नगर में मानसरोवर मेट्रो स्टेशन के पास स्थित है और मानसरोवर, श्याम नगर, बृजलालपुरा, गोपालपुरा बाइपास, किंग्स रोड और आसपास के जयपुर क्षेत्रों से आसानी से पहुँचा जा सकता है।"
      }
    },
    {
      "@type": "Question",
      "name": "क्या RNMH किंग्स रोड जयपुर के पास इमरजेंसी केयर देता है?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "हाँ। RNMH मेन किंग्स रोड, निर्माण नगर, जयपुर में 24x7 इमरजेंसी केयर उपलब्ध कराता है।"
      }
    },"""

    if "क्या R N Multispeciality Hospital" not in html:
        html = html.replace('"mainEntity": [', '"mainEntity": [\n' + hindi_faq_schema_items)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_english_homepage()
update_hindi_homepage()
print("Homepages updated.")
